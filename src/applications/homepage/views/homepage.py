import secrets
from io import BytesIO

import boto3
import pyqrcode
from django.urls import reverse_lazy
from django.views.generic import FormView
from dynaconf import settings as _ds

from applications.homepage.forms import UrlInputForm
from applications.homepage.models import Link
from applications.statistics.models import UTM, QRCode


class HomePageView(FormView):
    template_name = "homepage/homepage.html"
    form_class = UrlInputForm
    success_url = reverse_lazy("homepage:index")

    def get_initial(self):
        shortcut = self.request.session.get("shortcut")
        if shortcut:
            shortcut = shortcut.replace(self.request.scheme + "://", "")
        return {Link.original.field.name: shortcut}

    def form_valid(self, form):
        original = form.cleaned_data["original"]

        shortcut = self.request.headers["Referer"] + secrets.token_urlsafe(3)

        self.request.session["shortcut"] = shortcut
        self.request.session.set_expiry(0)

        url = Link(
            original=original,
            shortcut=shortcut,
            user_id=self.request.user.id,
            utm_copy=original,
        )
        url.save()
        url_id = url.id

        qr_code = pyqrcode.create(shortcut)
        buffer = BytesIO()
        qr_code.png(buffer, scale=8)
        buffer.seek(0)

        s3 = boto3.client(
            "s3",
            aws_access_key_id=_ds.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=_ds.AWS_SECRET_ACCESS_KEY,
        )
        s3.put_object(
            Body=buffer,
            Bucket="urlcutt",
            Key=f"{_ds.AWS_S3_CODES_LOCATION}/code-{url_id}.png",
            ACL="public-read",
        )

        qr = QRCode(
            original=f"{_ds.AWS_S3_CODES_LOCATION}/code-{url_id}.png", link_id=url_id
        )
        qr.save()

        utm = UTM(link_id=url_id)
        utm.save()

        return super().form_valid(form)

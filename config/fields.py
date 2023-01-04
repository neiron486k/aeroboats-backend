from django.db.models import FileField
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import filesizeformat
import os


class RestrictedFileField(FileField):
    def __init__(self, verbose_name=None, name=None, upload_to="", storage=None, **kwargs):
        self.max_upload_size = kwargs.pop("max_upload_size", 0) * 1024 * 1024
        self.extensions = kwargs.pop("extensions", [])

        super().__init__(verbose_name, name, upload_to, storage, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs["max_upload_size"] = self.max_upload_size
        kwargs["extensions"] = self.extensions

        return name, path, args, kwargs

    def clean(self, *args, **kwargs):
        data = super().clean(*args, **kwargs)
        file = data.file
        ext = os.path.splitext(str(file))[1]

        if file.size > self.max_upload_size:
            raise ValidationError(
                _("Please keep filesize under %s. Current filesize %s")
                % (filesizeformat(self.max_upload_size), filesizeformat(file.size))
            )

        if ext not in self.extensions:
            raise ValidationError(_("File not supported"))

        return data

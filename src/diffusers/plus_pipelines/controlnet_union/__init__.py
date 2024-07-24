#copied and modified from pipelines.controlnet.__init__.py
from typing import TYPE_CHECKING

from ...utils import (
    DIFFUSERS_SLOW_IMPORT,
    OptionalDependencyNotAvailable,
    _LazyModule,
    get_objects_from_module,
    is_flax_available,
    is_torch_available,
    is_transformers_available,
)


_dummy_objects = {}
_import_structure = {}

try:
    if not (is_transformers_available() and is_torch_available()):
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    from ...utils import dummy_torch_and_transformers_objects  # noqa F403

    _dummy_objects.update(get_objects_from_module(dummy_torch_and_transformers_objects))
else:
    _import_structure["pipeline_controlnet_union_inpaint_sd_xl"] = [
        "StableDiffusionXLControlNetUnionInpaintPipeline"
    ]
    _import_structure["pipeline_controlnet_union_sd_xl_img2img"] = [
        "StableDiffusionXLControlNetUnionImg2ImgPipeline"
    ]
    _import_structure["pipeline_controlnet_union_sd_xl"] = [
        "StableDiffusionXLControlNetUnionPipeline"
    ]


if TYPE_CHECKING or DIFFUSERS_SLOW_IMPORT:
    try:
        if not (is_transformers_available() and is_torch_available()):
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        from ...utils.dummy_torch_and_transformers_objects import *
    else:
        from .pipeline_controlnet_union_inpaint_sd_xl import StableDiffusionXLControlNetUnionInpaintPipeline
        from .pipeline_controlnet_union_sd_xl_img2img import StableDiffusionXLControlNetUnionImg2ImgPipeline
        from .pipeline_controlnet_union_sd_xl import StableDiffusionXLControlNetUnionPipeline



else:
    import sys

    sys.modules[__name__] = _LazyModule(
        __name__,
        globals()["__file__"],
        _import_structure,
        module_spec=__spec__,
    )
    for name, value in _dummy_objects.items():
        setattr(sys.modules[__name__], name, value)
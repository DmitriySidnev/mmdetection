from mmcv import ops
from .point_sample import (GridSampleOp, SimpleRoIAlign, generate_grid,
                          point_sample, rel_roi_point_to_rel_img_point, bilinear_grid_sample, point_sample_fn)


ops.SimpleRoIAlign = SimpleRoIAlign

__all__ = [
    'SimpleRoIAlign', 'generate_grid', 'point_sample',
    'rel_roi_point_to_rel_img_point', 'bilinear_grid_sample', 'GridSampleOp', 'point_sample_fn'
]
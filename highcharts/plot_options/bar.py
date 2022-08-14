from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts import constants, errors
from highcharts.decorators import class_sensitive, validate_types
from highcharts.plot_options.series import SeriesOptions
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern
from highcharts.utility_classes.data_grouping import DataGroupingOptions
from highcharts.utility_classes.partial_fill import PartialFillOptions


class BaseBarOptions(SeriesOptions):
    """Base class used for all bar/column types."""

    def __init__(self, **kwargs):
        self._border_color = None
        self._border_radius = None
        self._border_width = None
        self._center_in_category = None
        self._color_by_point = None
        self._colors = None
        self._grouping = None
        self._group_padding = None
        self._max_point_width = None
        self._min_point_length = None
        self._point_padding = None
        self._point_range = None
        self._point_width = None

        self.border_color = kwargs.pop('border_color', None)
        self.border_radius = kwargs.pop('border_radius', None)
        self.border_width = kwargs.pop('border_width', None)
        self.center_in_category = kwargs.pop('center_in_category', None)
        self.color_by_point = kwargs.pop('color_by_point', None)
        self.colors = kwargs.pop('colors', None)
        self.grouping = kwargs.pop('grouping', None)
        self.group_padding = kwargs.pop('group_padding', None)
        self.max_point_width = kwargs.pop('max_point_width', None)
        self.min_point_length = kwargs.pop('min_point_length', None)
        self.point_padding = kwargs.pop('point_padding', None)
        self.point_range = kwargs.pop('point_range', None)
        self.point_width = kwargs.pop('point_width', None)

        super(self).__init__(**kwargs)

    @property
    def border_color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the border surrounding each column or bar. Defaults to
        ``'#ffffff'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        from highcharts import utility_functions
        self._border_color = utility_functions.validate_color(value)

    @property
    def border_radius(self) -> Optional[int | float | Decimal]:
        """The corner radius of the border surrounding each column or bar. Defaults to
        ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_radius

    @border_radius.setter
    def border_radius(self, value):
        self._border_radius = validators.numeric(value,
                                                 allow_empty = True,
                                                 minimum = 0)

    @property
    def border_width(self) -> Optional[int | float | Decimal]:
        """The width of the border surrounding each column or bar. If
        :obj:`None <python:None>`, defaults to ``1`` when there is room for a border, but
        to ``0`` when the columns are so dense that a border would cover the next column.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_width

    @border_width.setter
    def border_width(self, value):
        self._border_width = validators.numeric(value,
                                                allow_empty = True,
                                                minimum = 0)

    @property
    def center_in_category(self) -> Optional[bool]:
        """If ``True``, the columns will center in the category, ignoring null or missing
        points. When ``False``, space will be reserved for null or missing points.
        Defaults to ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._center_in_category

    @center_in_category.setter
    def center_in_category(self, value):
        if value is None:
            self._center_in_category = None
        else:
            self._center_in_category = bool(value)

    @property
    def color_by_point(self) -> Optional[bool]:
        """When using automatic point colors pulled from the global colors or
        series-specific collections, this option determines whether the chart should
        receive one color per series (``False``) or one color per point (``True``).

        Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>
        """
        return self._color_by_point

    @color_by_point.setter
    def color_by_point(self, value):
        if value is None:
            self._color_by_point = None
        else:
            self._color_by_point = bool(value)

    @property
    def colors(self) -> Optional[List[str | Gradient | Pattern]]:
        """A series-specific or series type-specific color set to apply instead of the
        global colors when :meth:`BarOptions.color_by_point` is ``True``.

        :rtype: :class:`list <python:list>` of :class:`str <python:str>`,
          :class:`Gradient`, or :class:`Pattern` OR :obj:`None <python:None>`
        """
        return self._colors

    @colors.setter
    def colors(self, value):
        if not value:
            self._colors = None
        else:
            value = validators.iterable(value)
            checked_values = []
            for item in value:
                if isinstance(value, str):
                    checked_values.append(item)
                else:
                    processed_item = validate_types(item,
                                                    types = (Gradient, Pattern))
                    checked_values.append(processed_item)

            self._colors = checked_values

    @property
    def grouping(self) -> Optional[bool]:
        """If ``True``, groups non-stacked columns. If ``False``, renders them
        independent of each other. Non-grouped columns will be laid out individually and
        overlap each other.

        Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._grouping

    @grouping.setter
    def grouping(self, value):
        if value is None:
            self._grouping = None
        else:
            self._grouping = bool(value)

    @property
    def group_padding(self) -> Optional[int | float | Decimal]:
        """Padding between each value group, in x axis units. Defaults to ``0.2``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._group_padding

    @group_padding.setter
    def group_padding(self, value):
        self._group_padding = validators.numeric(value,
                                                 allow_empty = True,
                                                 minimum = 0)

    @property
    def max_point_width(self) -> Optional[int | float | Decimal]:
        """The maximum allowed pixel width for a column, translated to the height of a bar
        in a bar chart. This prevents the columns from becoming too wide when there is a
        small number of points in the chart. Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._max_point_width

    @max_point_width.setter
    def max_point_width(self, value):
        self._max_point_width = validators.numeric(value,
                                                   allow_empty = True,
                                                   minimum = 0)

    @property
    def min_point_length(self) -> Optional[int | float | Decimal]:
        """The minimal height for a column or width for a bar. Defaults to ``0``.

        By default, ``0`` values are not shown. To visualize a ``0`` (or close to zero)
        point, set the minimal point length to a pixel value like ``3``.

        .. warning::

          In stacked column charts, ``min_point_length`` might not be respected for
          tightly packed values.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._min_point_length

    @min_point_length.setter
    def min_point_length(self, value):
        self._min_point_length = validators.numeric(value,
                                                    allow_empty = True,
                                                    minimum = 0)

    @property
    def point_padding(self) -> Optional[int | float | Decimal]:
        """Padding between each column or bar, in x axis units. Defaults to ``0.1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._point_padding

    @point_padding.setter
    def point_padding(self, value):
        self._point_padding = validators.numeric(value,
                                                 allow_empty = True,
                                                 minimum = 0)

    @property
    def point_range(self) -> Optional[constants.EnforcedNullType | int | float | Decimal]:
        """The X axis range that each point is valid for, which determines the width of
        the column. Defaults to ``EnforcedNull``, which computes the range automatically.

        On a categorized axis, the range will be ``1`` by default (one category unit). On
        linear and datetime axes, the range will be computed as the distance between the
        two closest data points.

        The default ``EnforcedNull`` means it is computed automatically, but the setting
        can be used to override the default value.

        .. note::

          If :meth:`data_sorting <BarOptions.data_sorting>` is enabled, the default value
          is implicitly adjusted to ``1``.

        :rtype: numeric or :class:`EnforcedNullType` or :obj:`None <python:None>`
        """
        return self._point_range

    @point_range.setter
    def point_range(self, value):
        if isinstance(value, constants.EnforcedNullType):
            self._point_range = constants.EnforcedNull
        else:
            self._point_range = validators.numeric(value, allow_empty = True)

    @property
    def point_width(self) -> Optional[int | float | Decimal]:
        """A pixel value specifying a fixed width for each column or bar point. When set
        to :obj:`None <python:None>`, the width is calculated from the
        :meth:`point_padding <BarOptions.point_padding>` and
        :meth:`group_padding <BarOptions.group_padding>`. Defaults to
        :obj:`None <python:None>`.

        The width effects the dimension that is not based on the point value. For column
        series, this is the hoizontal length while for bar series it is the vertical
        length.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._point_width

    @point_width.setter
    def point_width(self, value):
        self._point_width = validators.numeric(value,
                                               allow_empty = True,
                                               minimum = 0)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'allow_point_select': as_dict.pop('allowPointSelect', None),
            'animation': as_dict.pop('animation', None),
            'class_name': as_dict.pop('className', None),
            'clip': as_dict.pop('clip', None),
            'color': as_dict.pop('color', None),
            'cursor': as_dict.pop('cursor', None),
            'custom': as_dict.pop('custom', None),
            'dash_style': as_dict.pop('dashStyle', None),
            'data_labels': as_dict.pop('dataLabels', None),
            'description': as_dict.pop('description', None),
            'enable_mouse_tracking': as_dict.pop('enableMouseTracking', None),
            'events': as_dict.pop('events', None),
            'include_in_data_export': as_dict.pop('includeInDataExport', None),
            'keys': as_dict.pop('keys', None),
            'label': as_dict.pop('label', None),
            'linked_to': as_dict.pop('linkedTo', None),
            'marker': as_dict.pop('marker', None),
            'on_point': as_dict.pop('onPoint', None),
            'opacity': as_dict.pop('opacity', None),
            'point': as_dict.pop('point', None),
            'point_description_formatter': as_dict.pop('pointDescriptionFormatter', None),
            'selected': as_dict.pop('selected', None),
            'show_checkbox': as_dict.pop('showCheckbox', None),
            'show_in_legend': as_dict.pop('showInLegend', None),
            'skip_keyboard_navigation': as_dict.pop('skipKeyboardNavigation', None),
            'states': as_dict.pop('states', None),
            'threshold': as_dict.pop('threshold', None),
            'tooltip': as_dict.pop('tooltip', None),
            'turbo_threshold': as_dict.pop('turboThreshold', None),
            'visible': as_dict.pop('visible', None),

            'animation_limit': as_dict.pop('animationLimit', None),
            'boost_blending': as_dict.pop('boostBlending', None),
            'boost_threshold': as_dict.pop('boostThreshold', None),
            'color_axis': as_dict.pop('colorAxis', None),
            'color_index': as_dict.pop('colorIndex', None),
            'color_key': as_dict.pop('colorKey', None),
            'connect_ends': as_dict.pop('connectEnds', None),
            'connect_nulls': as_dict.pop('connectNulls', None),
            'crisp': as_dict.pop('crisp', None),
            'crop_threshold': as_dict.pop('cropThreshold', None),
            'data_sorting': as_dict.pop('dataSorting', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'find_nearest_point_by': as_dict.pop('findNearestPointBy', None),
            'get_extremes_for_all': as_dict.pop('getExtremesForAll', None),
            'linecap': as_dict.pop('linecap', None),
            'line_width': as_dict.pop('lineWidth', None),
            'negative_color': as_dict.pop('negativeColor', None),
            'point_interval': as_dict.pop('pointInterval', None),
            'point_interval_unit': as_dict.pop('pointIntervalUnit', None),
            'point_placement': as_dict.pop('pointPlacement', None),
            'point_start': as_dict.pop('pointStart', None),
            'relative_x_value': as_dict.pop('relativeXValue', None),
            'shadow': as_dict.pop('shadow', None),
            'soft_threshold': as_dict.pop('softThreshold', None),
            'stacking': as_dict.pop('stacking', None),
            'step': as_dict.pop('step', None),
            'zone_axis': as_dict.pop('zoneAxis', None),
            'zones': as_dict.pop('zones', None),

            'border_color': as_dict.pop('borderColor', None),
            'border_radius': as_dict.pop('borderRadius', None),
            'border_width': as_dict.pop('borderWidth', None),
            'center_in_category': as_dict.pop('centerInCategory', None),
            'color_by_point': as_dict.pop('colorByPoint', None),
            'colors': as_dict.pop('colors', None),
            'grouping': as_dict.pop('grouping', None),
            'group_padding': as_dict.pop('groupPadding', None),
            'max_point_width': as_dict.pop('maxPointWidth', None),
            'min_point_length': as_dict.pop('minPointLength', None),
            'point_padding': as_dict.pop('pointPadding', None),
            'point_range': as_dict.pop('pointRange', None),
            'point_width': as_dict.pop('pointWidth', None)
        }

        return kwargs

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'borderColor': self.border_color,
            'borderRadius': self.border_radius,
            'borderWidth': self.border_width,
            'centerInCategory': self.center_in_category,
            'colorByPoint': self.color_by_point,
            'colors': self.colors,
            'grouping': self.grouping,
            'groupPadding': self.group_padding,
            'maxPointWidth': self.max_point_width,
            'minPointLength': self.min_point_length,
            'pointPadding': self.point_padding,
            'pointRange': self.point_range,
            'pointWidth': self.point_width
        }
        parent_as_dict = super(self)._to_untrimmed_dict()

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class BarOptions(BaseBarOptions):
    """General options to apply to all Bar series types. A bar series is a special
    type of column series where the columns are horizontal.

    .. figure:: _static/bar-example.png
      :alt: Bar Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._depth = None
        self._edge_color = None
        self._edge_width = None
        self._group_z_padding = None

        self.depth = kwargs.pop('depth', None)
        self.edge_color = kwargs.pop('edge_color', None)
        self.edge_width = kwargs.pop('edge_width', None)
        self.group_z_padding = kwargs.pop('group_z_padding', None)

        super(self).__init__(**kwargs)

    @property
    def depth(self) -> Optional[int | float | Decimal]:
        """Depth of the columns in a 3D column chart. Defaults to ``25``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._depth

    @depth.setter
    def depth(self, value):
        self._depth = validators.numeric(value,
                                         allow_empty = True,
                                         minimum = 0)

    @property
    def edge_color(self) -> Optional[str]:
        """The color of the edges when rendering 3D columns. Defaults to
        :obj:`None <python:None>`.

        Similar to :meth:`border_color <BarOptions.border_color>`, except it defaults to
        the same color as the column if set to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._edge_color

    @edge_color.setter
    def edge_color(self, value):
        self._edge_color = validators.string(value, allow_empty = True)

    @property
    def edge_width(self) -> Optional[int | float | Decimal]:
        """The width of the colored edges applied to a 3D column. Defaults to ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._edge_width

    @edge_width.setter
    def edge_width(self, value):
        self._edge_width = validators.numeric(value,
                                              allow_empty = True,
                                              minimum = 0)

    @property
    def group_z_padding(self) -> Optional[int | float | Decimal]:
        """Spacing between columns along the Z axis in a 3D chart. Defaults to ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._group_z_padding

    @group_z_padding.setter
    def group_z_padding(self, value):
        self._group_z_padding = validators.numeric(value,
                                                   allow_empty = True,
                                                   minimum = 0)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'allow_point_select': as_dict.pop('allowPointSelect', None),
            'animation': as_dict.pop('animation', None),
            'class_name': as_dict.pop('className', None),
            'clip': as_dict.pop('clip', None),
            'color': as_dict.pop('color', None),
            'cursor': as_dict.pop('cursor', None),
            'custom': as_dict.pop('custom', None),
            'dash_style': as_dict.pop('dashStyle', None),
            'data_labels': as_dict.pop('dataLabels', None),
            'description': as_dict.pop('description', None),
            'enable_mouse_tracking': as_dict.pop('enableMouseTracking', None),
            'events': as_dict.pop('events', None),
            'include_in_data_export': as_dict.pop('includeInDataExport', None),
            'keys': as_dict.pop('keys', None),
            'label': as_dict.pop('label', None),
            'linked_to': as_dict.pop('linkedTo', None),
            'marker': as_dict.pop('marker', None),
            'on_point': as_dict.pop('onPoint', None),
            'opacity': as_dict.pop('opacity', None),
            'point': as_dict.pop('point', None),
            'point_description_formatter': as_dict.pop('pointDescriptionFormatter', None),
            'selected': as_dict.pop('selected', None),
            'show_checkbox': as_dict.pop('showCheckbox', None),
            'show_in_legend': as_dict.pop('showInLegend', None),
            'skip_keyboard_navigation': as_dict.pop('skipKeyboardNavigation', None),
            'states': as_dict.pop('states', None),
            'threshold': as_dict.pop('threshold', None),
            'tooltip': as_dict.pop('tooltip', None),
            'turbo_threshold': as_dict.pop('turboThreshold', None),
            'visible': as_dict.pop('visible', None),

            'animation_limit': as_dict.pop('animationLimit', None),
            'boost_blending': as_dict.pop('boostBlending', None),
            'boost_threshold': as_dict.pop('boostThreshold', None),
            'color_axis': as_dict.pop('colorAxis', None),
            'color_index': as_dict.pop('colorIndex', None),
            'color_key': as_dict.pop('colorKey', None),
            'connect_ends': as_dict.pop('connectEnds', None),
            'connect_nulls': as_dict.pop('connectNulls', None),
            'crisp': as_dict.pop('crisp', None),
            'crop_threshold': as_dict.pop('cropThreshold', None),
            'data_sorting': as_dict.pop('dataSorting', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'find_nearest_point_by': as_dict.pop('findNearestPointBy', None),
            'get_extremes_for_all': as_dict.pop('getExtremesForAll', None),
            'linecap': as_dict.pop('linecap', None),
            'line_width': as_dict.pop('lineWidth', None),
            'negative_color': as_dict.pop('negativeColor', None),
            'point_interval': as_dict.pop('pointInterval', None),
            'point_interval_unit': as_dict.pop('pointIntervalUnit', None),
            'point_placement': as_dict.pop('pointPlacement', None),
            'point_start': as_dict.pop('pointStart', None),
            'relative_x_value': as_dict.pop('relativeXValue', None),
            'shadow': as_dict.pop('shadow', None),
            'soft_threshold': as_dict.pop('softThreshold', None),
            'stacking': as_dict.pop('stacking', None),
            'step': as_dict.pop('step', None),
            'zone_axis': as_dict.pop('zoneAxis', None),
            'zones': as_dict.pop('zones', None),

            'border_color': as_dict.pop('borderColor', None),
            'border_radius': as_dict.pop('borderRadius', None),
            'border_width': as_dict.pop('borderWidth', None),
            'center_in_category': as_dict.pop('centerInCategory', None),
            'color_by_point': as_dict.pop('colorByPoint', None),
            'colors': as_dict.pop('colors', None),
            'grouping': as_dict.pop('grouping', None),
            'group_padding': as_dict.pop('groupPadding', None),
            'max_point_width': as_dict.pop('maxPointWidth', None),
            'min_point_length': as_dict.pop('minPointLength', None),
            'point_padding': as_dict.pop('pointPadding', None),
            'point_range': as_dict.pop('pointRange', None),
            'point_width': as_dict.pop('pointWidth', None),

            'depth': as_dict.pop('depth', None),
            'edge_color': as_dict.pop('edgeColor', None),
            'edge_width': as_dict.pop('edgeWidth', None),
            'group_z_padding': as_dict.pop('groupZPadding', None)
         }

        return kwargs

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'depth': self.depth,
            'edgeColor': self.edge_color,
            'edgeWidth': self.edge_width,
            'groupZPadding': self.group_z_padding
        }
        parent_as_dict = super(self)._to_untrimmed_dict()

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class ColumnOptions(BarOptions):
    """General options to apply to all Column series types.

    Column series display one column per value along an X axis.

    .. figure:: _static/column-example.png
      :alt: Column Example Chart
      :align: center

    """
    pass


class ColumnPyramidOptions(ColumnOptions):
    """General options to apply to all Column Pyramid series types.

    Column Pyramid series display one pyramid per value along an X axis.

    .. hint::

      To display horizontal pyramids, set :meth:`Chart.inverted` to ``True``.

    .. tabs::

      .. tab:: Standard

        .. figure:: _static/columnpyramid-example.png
          :alt: ColumnPyramid Example Chart
          :align: center

      .. tab:: Stacked

        .. figure:: _static/columnpyramid-example-stacked.png
          :alt: Stacked Column Pyramid Example Chart
          :align: center

      .. tab:: Stacked + Inverted

        .. figure:: _static/columnpyramid-example-stacked-horizontal.png
          :alt: Stacked and Inverted Column Pyramid Example Chart
          :align: center

    """
    pass


class ColumnRangeOptions(ColumnOptions):
    """General options to apply to all Column Range series types.

    The column range is a cartesian series type with higher and lower Y values along
    an X axis.

    .. hint::

      To display horizontal bars, set :meth:`Chart.inverted` to ``True``.

    .. tabs::

      .. tab:: Standard

        .. figure:: _static/columnrange-example.png
          :alt: ColumnRange Example Chart
          :align: center

      .. tab:: Horizontal

        .. figure:: _static/columnrange-example-horizontal.png
          :alt: Inverted Column Range Example Chart
          :align: center

    """
    pass


class CylinderOptions(BarOptions):
    """General options to apply to all Cylinder series types.

    A cylinder graph is a variation of a 3d column graph. The cylinder graph features
    cylindrical points.

    .. figure:: _static/cylinder-example.png
      :alt: Cylinder Example Chart
      :align: center

    """
    pass


class VariwideOptions(BaseBarOptions):
    """General options to apply to all Variwide series types.

    A variwide chart (related to marimekko chart) is a column chart with a variable
    width expressing a third dimension.

    .. tabs::

      .. tab:: Standard Variwide

        .. figure:: _static/variwide-example.png
          :alt: Variwide Example Chart
          :align: center

      .. tab:: Inverted Variwide

        .. figure:: _static/variwide-example-inverted.png
          :alt: Variwide Example Chart
          :align: center

      .. tab:: with Datetime Axis

        .. figure:: _static/variwide-example-datetime.png
          :alt: Variwide Example Chart
          :align: center

    """
    pass


class WaterfallOptions(ColumnOptions):
    """General options to apply to all Waterfall series types.

    A waterfall chart displays sequentially introduced positive or negative values in
    cumulative columns.

    .. tabs::

      .. tab:: Standard Waterfall

        .. figure:: _static/waterfall-example.png
          :alt: Waterfall Example Chart
          :align: center

      .. tab:: Horizontal (Inverted) Waterfall

        .. figure:: _static/waterfall-example-inverted.png
          :alt: Waterfall Example Chart
          :align: center

      .. tab:: Stacked Waterfall

        .. figure:: _static/waterfall-example-stacked.png
          :alt: Waterfall Example Chart
          :align: center

    """

    def __init__(self, **kwargs):
        self._line_color = None
        self._up_color = None

        self.line_color = kwargs.pop('line_color', None)
        self.up_color = kwargs.pop('up_color', None)

        super().__init__(**kwargs)

    @property
    def line_color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the line that connects columns in a waterfall series. Defaults to
        ``'#333333'``.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`str <python:str>`
        """
        return self._line_color

    @line_color.setter
    def line_color(self, value):
        from highcharts import utility_functions
        self._line_color = utility_functions.validate_color(value)

    @property
    def up_color(self) -> Optional[str | Gradient | Pattern]:
        """The color used specifically for positive point columns. When
        :obj:`None <python:None>`, the general series color is used. Defaults to
        :obj:`None <python:None>`.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`str <python:str>`
        """
        return self._up_color

    @up_color.setter
    def up_color(self, value):
        from highcharts import utility_functions
        self._up_color = utility_functions.validate_color(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'allow_point_select': as_dict.pop('allowPointSelect', None),
            'animation': as_dict.pop('animation', None),
            'class_name': as_dict.pop('className', None),
            'clip': as_dict.pop('clip', None),
            'color': as_dict.pop('color', None),
            'cursor': as_dict.pop('cursor', None),
            'custom': as_dict.pop('custom', None),
            'dash_style': as_dict.pop('dashStyle', None),
            'data_labels': as_dict.pop('dataLabels', None),
            'description': as_dict.pop('description', None),
            'enable_mouse_tracking': as_dict.pop('enableMouseTracking', None),
            'events': as_dict.pop('events', None),
            'include_in_data_export': as_dict.pop('includeInDataExport', None),
            'keys': as_dict.pop('keys', None),
            'label': as_dict.pop('label', None),
            'linked_to': as_dict.pop('linkedTo', None),
            'marker': as_dict.pop('marker', None),
            'on_point': as_dict.pop('onPoint', None),
            'opacity': as_dict.pop('opacity', None),
            'point': as_dict.pop('point', None),
            'point_description_formatter': as_dict.pop('pointDescriptionFormatter', None),
            'selected': as_dict.pop('selected', None),
            'show_checkbox': as_dict.pop('showCheckbox', None),
            'show_in_legend': as_dict.pop('showInLegend', None),
            'skip_keyboard_navigation': as_dict.pop('skipKeyboardNavigation', None),
            'states': as_dict.pop('states', None),
            'threshold': as_dict.pop('threshold', None),
            'tooltip': as_dict.pop('tooltip', None),
            'turbo_threshold': as_dict.pop('turboThreshold', None),
            'visible': as_dict.pop('visible', None),

            'animation_limit': as_dict.pop('animationLimit', None),
            'boost_blending': as_dict.pop('boostBlending', None),
            'boost_threshold': as_dict.pop('boostThreshold', None),
            'color_axis': as_dict.pop('colorAxis', None),
            'color_index': as_dict.pop('colorIndex', None),
            'color_key': as_dict.pop('colorKey', None),
            'connect_ends': as_dict.pop('connectEnds', None),
            'connect_nulls': as_dict.pop('connectNulls', None),
            'crisp': as_dict.pop('crisp', None),
            'crop_threshold': as_dict.pop('cropThreshold', None),
            'data_sorting': as_dict.pop('dataSorting', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'find_nearest_point_by': as_dict.pop('findNearestPointBy', None),
            'get_extremes_for_all': as_dict.pop('getExtremesForAll', None),
            'linecap': as_dict.pop('linecap', None),
            'line_width': as_dict.pop('lineWidth', None),
            'negative_color': as_dict.pop('negativeColor', None),
            'point_interval': as_dict.pop('pointInterval', None),
            'point_interval_unit': as_dict.pop('pointIntervalUnit', None),
            'point_placement': as_dict.pop('pointPlacement', None),
            'point_start': as_dict.pop('pointStart', None),
            'relative_x_value': as_dict.pop('relativeXValue', None),
            'shadow': as_dict.pop('shadow', None),
            'soft_threshold': as_dict.pop('softThreshold', None),
            'stacking': as_dict.pop('stacking', None),
            'step': as_dict.pop('step', None),
            'zone_axis': as_dict.pop('zoneAxis', None),
            'zones': as_dict.pop('zones', None),

            'border_color': as_dict.pop('borderColor', None),
            'border_radius': as_dict.pop('borderRadius', None),
            'border_width': as_dict.pop('borderWidth', None),
            'center_in_category': as_dict.pop('centerInCategory', None),
            'color_by_point': as_dict.pop('colorByPoint', None),
            'colors': as_dict.pop('colors', None),
            'grouping': as_dict.pop('grouping', None),
            'group_padding': as_dict.pop('groupPadding', None),
            'max_point_width': as_dict.pop('maxPointWidth', None),
            'min_point_length': as_dict.pop('minPointLength', None),
            'point_padding': as_dict.pop('pointPadding', None),
            'point_range': as_dict.pop('pointRange', None),
            'point_width': as_dict.pop('pointWidth', None),

            'depth': as_dict.pop('depth', None),
            'edge_color': as_dict.pop('edgeColor', None),
            'edge_width': as_dict.pop('edgeWidth', None),
            'group_z_padding': as_dict.pop('groupZPadding', None),

            'line_color': as_dict.pop('lineColor', None),
            'up_color': as_dict.pop('upColor', None)
         }

        return kwargs

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'lineColor': self.line_color,
            'upColor': self.up_color
        }
        parent_as_dict = super(self)._to_untrimmed_dict()

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class WindBarbOptions(BarOptions):
    """General options to apply to all Wind Barb series types.

    Wind barbs are a convenient way to represent wind speed and direction in one
    graphical form. Wind direction is given by the stem direction, and wind speed by
    the number and shape of barbs.

    .. figure:: _static/windbarb-example.png
      :alt: Wind Barb Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._data_grouping = None
        self._on_series = None
        self._vector_length = None
        self._x_offset = None
        self._y_offset = None

        self.data_grouping = kwargs.pop('data_grouping', None)
        self.on_series = kwargs.pop('on_series', None)
        self.vector_length = kwargs.pop('vector_length', None)
        self.x_offset = kwargs.pop('x_offset', None)
        self.y_offset = kwargs.pop('y_offset', None)

        super().__init__(**kwargs)

    @property
    def data_grouping(self) -> Optional[DataGroupingOptions]:
        """Data grouping options for the wind barbs. Defaults to
        :obj:`None <python:None>`.

        .. warning::

          In Highcharts, this requires the ``modules/datagrouping.js`` module to be
          loaded. In Highcharts Stock, data grouping is included.

        :rtype: :class:`DataGroupingOptions` or :obj:`None <python:None>`
        """
        return self._data_grouping

    @data_grouping.setter
    @class_sensitive(DataGroupingOptions)
    def data_grouping(self, value):
        self._data_grouping = value

    @property
    def on_series(self) -> Optional[str]:
        """The id of another series in the chart that the wind barbs are projected on.
        When :obj:`None <python:None>`, the wind symbols are drawn on the X axis, but
        offset up or down by the :meth:`WindbarbOptions.y_offset` setting.

        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._on_series

    @on_series.setter
    def on_series(self, value):
        self._on_series = validators.string(value, allow_empty = True)

    @property
    def vector_length(self) -> Optional[int | float | Decimal]:
        """Length of the windbarb stems, expressed in pixels. Defaults to ``20``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._vector_length

    @vector_length.setter
    def vector_length(self, value):
        self._vector_length = validators.numeric(value,
                                                 allow_empty = True,
                                                 minimum = 0)

    @property
    def x_offset(self) -> Optional[int | float | Decimal]:
        """Horizontal offset from the cartesian position, in pixels. Defaults to ``0``.

        .. note::

          When the chart is inverted, this option allows translation similar to
          :meth:`WindbarbOptions.y_offset` in non-inverted charts.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._x_offset

    @x_offset.setter
    def x_offset(self, value):
        self._x_offset = validators.numeric(value, allow_empty = True)

    @property
    def y_offset(self) -> Optional[int | float | Decimal]:
        """Vertical offset from the cartesian position, in pixels. Defaults to ``-20``.

        .. note::

          The default value makes sure the symbols don't overlap the X axis when
          :meth:`WindbarbOptions.on_series` is :obj:`None <python:None>`, and that they
          don't overlap the linked series when :meth:`Windbarb.on_series` is provided.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._y_offset

    @y_offset.setter
    def y_offset(self, value):
        self._y_offset = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'allow_point_select': as_dict.pop('allowPointSelect', None),
            'animation': as_dict.pop('animation', None),
            'class_name': as_dict.pop('className', None),
            'clip': as_dict.pop('clip', None),
            'color': as_dict.pop('color', None),
            'cursor': as_dict.pop('cursor', None),
            'custom': as_dict.pop('custom', None),
            'dash_style': as_dict.pop('dashStyle', None),
            'data_labels': as_dict.pop('dataLabels', None),
            'description': as_dict.pop('description', None),
            'enable_mouse_tracking': as_dict.pop('enableMouseTracking', None),
            'events': as_dict.pop('events', None),
            'include_in_data_export': as_dict.pop('includeInDataExport', None),
            'keys': as_dict.pop('keys', None),
            'label': as_dict.pop('label', None),
            'linked_to': as_dict.pop('linkedTo', None),
            'marker': as_dict.pop('marker', None),
            'on_point': as_dict.pop('onPoint', None),
            'opacity': as_dict.pop('opacity', None),
            'point': as_dict.pop('point', None),
            'point_description_formatter': as_dict.pop('pointDescriptionFormatter', None),
            'selected': as_dict.pop('selected', None),
            'show_checkbox': as_dict.pop('showCheckbox', None),
            'show_in_legend': as_dict.pop('showInLegend', None),
            'skip_keyboard_navigation': as_dict.pop('skipKeyboardNavigation', None),
            'states': as_dict.pop('states', None),
            'threshold': as_dict.pop('threshold', None),
            'tooltip': as_dict.pop('tooltip', None),
            'turbo_threshold': as_dict.pop('turboThreshold', None),
            'visible': as_dict.pop('visible', None),

            'animation_limit': as_dict.pop('animationLimit', None),
            'boost_blending': as_dict.pop('boostBlending', None),
            'boost_threshold': as_dict.pop('boostThreshold', None),
            'color_axis': as_dict.pop('colorAxis', None),
            'color_index': as_dict.pop('colorIndex', None),
            'color_key': as_dict.pop('colorKey', None),
            'connect_ends': as_dict.pop('connectEnds', None),
            'connect_nulls': as_dict.pop('connectNulls', None),
            'crisp': as_dict.pop('crisp', None),
            'crop_threshold': as_dict.pop('cropThreshold', None),
            'data_sorting': as_dict.pop('dataSorting', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'find_nearest_point_by': as_dict.pop('findNearestPointBy', None),
            'get_extremes_for_all': as_dict.pop('getExtremesForAll', None),
            'linecap': as_dict.pop('linecap', None),
            'line_width': as_dict.pop('lineWidth', None),
            'negative_color': as_dict.pop('negativeColor', None),
            'point_interval': as_dict.pop('pointInterval', None),
            'point_interval_unit': as_dict.pop('pointIntervalUnit', None),
            'point_placement': as_dict.pop('pointPlacement', None),
            'point_start': as_dict.pop('pointStart', None),
            'relative_x_value': as_dict.pop('relativeXValue', None),
            'shadow': as_dict.pop('shadow', None),
            'soft_threshold': as_dict.pop('softThreshold', None),
            'stacking': as_dict.pop('stacking', None),
            'step': as_dict.pop('step', None),
            'zone_axis': as_dict.pop('zoneAxis', None),
            'zones': as_dict.pop('zones', None),

            'border_color': as_dict.pop('borderColor', None),
            'border_radius': as_dict.pop('borderRadius', None),
            'border_width': as_dict.pop('borderWidth', None),
            'center_in_category': as_dict.pop('centerInCategory', None),
            'color_by_point': as_dict.pop('colorByPoint', None),
            'colors': as_dict.pop('colors', None),
            'grouping': as_dict.pop('grouping', None),
            'group_padding': as_dict.pop('groupPadding', None),
            'max_point_width': as_dict.pop('maxPointWidth', None),
            'min_point_length': as_dict.pop('minPointLength', None),
            'point_padding': as_dict.pop('pointPadding', None),
            'point_range': as_dict.pop('pointRange', None),
            'point_width': as_dict.pop('pointWidth', None),

            'depth': as_dict.pop('depth', None),
            'edge_color': as_dict.pop('edgeColor', None),
            'edge_width': as_dict.pop('edgeWidth', None),
            'group_z_padding': as_dict.pop('groupZPadding', None),

            'data_grouping': as_dict.pop('dataGrouping', None),
            'on_series': as_dict.pop('onSeries', None),
            'vector_length': as_dict.pop('vectorLength', None),
            'x_offset': as_dict.pop('xOffset', None),
            'y_offset': as_dict.pop('yOffset', None)
         }

        return kwargs

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'dataGrouping': self.data_grouping,
            'onSeries': self.on_series,
            'vectorLength': self.vector_length,
            'xOffset': self.x_offset,
            'yOffset': self.y_offset,
        }
        parent_as_dict = super(self)._to_untrimmed_dict()

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class XRangeOptions(BaseBarOptions):
    """General options to apply to all X-Range series types.

    The X-range series displays ranges on the X axis, typically time intervals with a
    start and end date.

    .. tabs::

      .. tab:: Standard X-Range

        .. figure:: _static/xrange-example.png
          :alt: X-Range Example Chart
          :align: center

      .. tab:: Inverted X-Range

        .. figure:: _static/xrange-example-inverted.png
          :alt: Inverted X-Range Example Chart
          :align: center

    """

    def __init__(self, **kwargs):
        self._group_z_padding = None
        self._partial_fill = None

        self.group_z_padding = kwargs.pop('group_z_padding', None)
        self.partial_fill = kwargs.pop('partial_fill', None)

        super().__init__(**kwargs)

    @property
    def group_z_padding(self) -> Optional[int | float | Decimal]:
        """Spacing between columns along the Z axis in a 3D chart. Defaults to ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._group_z_padding

    @group_z_padding.setter
    def group_z_padding(self, value):
        self._group_z_padding = validators.numeric(value,
                                                   allow_empty = True,
                                                   minimum = 0)

    @property
    def partial_fill(self) -> Optional[PartialFillOptions]:
        """A partial fill for each point, typically used to visualize how much of a task
        is performed.

        .. note::

          The partial fill object can be set either on series or point level.

        :rtype: :class:`PartialFillOptions` or :obj:`None <python:None>`
        """
        return self._partial_fill

    @partial_fill.setter
    @class_sensitive(PartialFillOptions)
    def partial_fill(self, value):
        self._partial_fill = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'allow_point_select': as_dict.pop('allowPointSelect', None),
            'animation': as_dict.pop('animation', None),
            'class_name': as_dict.pop('className', None),
            'clip': as_dict.pop('clip', None),
            'color': as_dict.pop('color', None),
            'cursor': as_dict.pop('cursor', None),
            'custom': as_dict.pop('custom', None),
            'dash_style': as_dict.pop('dashStyle', None),
            'data_labels': as_dict.pop('dataLabels', None),
            'description': as_dict.pop('description', None),
            'enable_mouse_tracking': as_dict.pop('enableMouseTracking', None),
            'events': as_dict.pop('events', None),
            'include_in_data_export': as_dict.pop('includeInDataExport', None),
            'keys': as_dict.pop('keys', None),
            'label': as_dict.pop('label', None),
            'linked_to': as_dict.pop('linkedTo', None),
            'marker': as_dict.pop('marker', None),
            'on_point': as_dict.pop('onPoint', None),
            'opacity': as_dict.pop('opacity', None),
            'point': as_dict.pop('point', None),
            'point_description_formatter': as_dict.pop('pointDescriptionFormatter', None),
            'selected': as_dict.pop('selected', None),
            'show_checkbox': as_dict.pop('showCheckbox', None),
            'show_in_legend': as_dict.pop('showInLegend', None),
            'skip_keyboard_navigation': as_dict.pop('skipKeyboardNavigation', None),
            'states': as_dict.pop('states', None),
            'threshold': as_dict.pop('threshold', None),
            'tooltip': as_dict.pop('tooltip', None),
            'turbo_threshold': as_dict.pop('turboThreshold', None),
            'visible': as_dict.pop('visible', None),

            'animation_limit': as_dict.pop('animationLimit', None),
            'boost_blending': as_dict.pop('boostBlending', None),
            'boost_threshold': as_dict.pop('boostThreshold', None),
            'color_axis': as_dict.pop('colorAxis', None),
            'color_index': as_dict.pop('colorIndex', None),
            'color_key': as_dict.pop('colorKey', None),
            'connect_ends': as_dict.pop('connectEnds', None),
            'connect_nulls': as_dict.pop('connectNulls', None),
            'crisp': as_dict.pop('crisp', None),
            'crop_threshold': as_dict.pop('cropThreshold', None),
            'data_sorting': as_dict.pop('dataSorting', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'find_nearest_point_by': as_dict.pop('findNearestPointBy', None),
            'get_extremes_for_all': as_dict.pop('getExtremesForAll', None),
            'linecap': as_dict.pop('linecap', None),
            'line_width': as_dict.pop('lineWidth', None),
            'negative_color': as_dict.pop('negativeColor', None),
            'point_interval': as_dict.pop('pointInterval', None),
            'point_interval_unit': as_dict.pop('pointIntervalUnit', None),
            'point_placement': as_dict.pop('pointPlacement', None),
            'point_start': as_dict.pop('pointStart', None),
            'relative_x_value': as_dict.pop('relativeXValue', None),
            'shadow': as_dict.pop('shadow', None),
            'soft_threshold': as_dict.pop('softThreshold', None),
            'stacking': as_dict.pop('stacking', None),
            'step': as_dict.pop('step', None),
            'zone_axis': as_dict.pop('zoneAxis', None),
            'zones': as_dict.pop('zones', None),

            'border_color': as_dict.pop('borderColor', None),
            'border_radius': as_dict.pop('borderRadius', None),
            'border_width': as_dict.pop('borderWidth', None),
            'center_in_category': as_dict.pop('centerInCategory', None),
            'color_by_point': as_dict.pop('colorByPoint', None),
            'colors': as_dict.pop('colors', None),
            'grouping': as_dict.pop('grouping', None),
            'group_padding': as_dict.pop('groupPadding', None),
            'max_point_width': as_dict.pop('maxPointWidth', None),
            'min_point_length': as_dict.pop('minPointLength', None),
            'point_padding': as_dict.pop('pointPadding', None),
            'point_range': as_dict.pop('pointRange', None),
            'point_width': as_dict.pop('pointWidth', None),

            'group_z_padding': as_dict.pop('groupZPadding', None),
            'partial_fill': as_dict.pop('partialFill', None)
         }

        return kwargs

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'groupZPadding': self.group_z_padding,
            'partialFill': self.partial_fill
        }
        parent_as_dict = super(self)._to_untrimmed_dict()

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed

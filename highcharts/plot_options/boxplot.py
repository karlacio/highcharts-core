from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts import constants, errors
from highcharts.decorators import class_sensitive
from highcharts.plot_options.bar import BarOptions
from highcharts.plot_options.drag_drop import BoxPlotDragDropOptions
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern


class BoxPlotOptions(BarOptions):
    """General options to apply to all Box Plot series types.

    A box plot is a convenient way of depicting groups of data through their
    five-number summaries:

      * the smallest observation (sample minimum),
      * lower quartile (Q1),
      * median (Q2),
      * upper quartile (Q3), and
      * largest observation (sample maximum).

    .. figure:: _static/boxplot-example.png
      :alt: Box Plot Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._box_dash_style = None
        self._median_color = None
        self._median_dash_style = None
        self._median_width = None
        self._stem_dash_style = None
        self._stem_width = None
        self._whisker_color = None
        self._whisker_dash_style = None
        self._whisker_length = None
        self._whisker_width = None

        self.box_dash_style = kwargs.pop('box_dash_style', None)
        self.median_color = kwargs.pop('median_color', None)
        self.median_dash_style = kwargs.pop('median_dash_style', None)
        self.median_width = kwargs.pop('median_width', None)
        self.stem_dash_style = kwargs.pop('stem_dash_style', None)
        self.stem_width = kwargs.pop('stem_width', None)
        self.whisker_color = kwargs.pop('whisker_color', None)
        self.whisker_dash_style = kwargs.pop('whisker_dash_style', None)
        self.whisker_length = kwargs.pop('whisker_length', None)
        self.whisker_width = kwargs.pop('whisker_width', None)

        super(self).__init__(**kwargs)

    @property
    def box_dash_style(self) -> Optional[str]:
        """The dash style of the box.

        Accepts one of the following values:

          * 'Dash',
          * 'DashDot',
          * 'Dot',
          * 'LongDash',
          * 'LongDashDot',
          * 'LongDashDotDot',
          * 'ShortDash',
          * 'ShortDashDot',
          * 'ShortDashDotDot',
          * 'ShortDot',
          * 'Solid'

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._box_dash_style

    @box_dash_style.setter
    def box_dash_style(self, value):
        if not value:
            self._box_dash_style = None
        else:
            value = validators.string(value)
            if value not in constants.SUPPORTED_DASH_STYLE_VALUES:
                raise errors.HighchartsValueError(f'box_dash_style expects a recognized '
                                                  f'value, but received: {value}')
            self._box_dash_style = value

    @property
    def drag_drop(self) -> Optional[BoxPlotDragDropOptions]:
        """The draggable-points module allows points to be moved around or modified in the
        chart.

        In addition to the options mentioned under the dragDrop API structure, the module
        fires three (JavaScript) events:

          * ``point.dragStart``
          * ``point.drag``
          * ``point.drop``

        :rtype: :class:`DragDropOptions` or :obj:`None <python:None>`
        """
        return self._drag_drop

    @drag_drop.setter
    @class_sensitive(BoxPlotDragDropOptions)
    def drag_drop(self, value):
        self._drag_drop = value

    @property
    def median_color(self) -> Optional[str | Gradient]:
        """The color of the median line. If :obj:`None <python:None>`, the general series
        color applies. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, or :obj:`None <python:None>`
        """
        return self._median_color

    @median_color.setter
    def median_color(self, value):
        from highcharts import utility_functions
        self._median_color = utility_functions.validate_color(value)

    @property
    def median_dash_style(self) -> Optional[str]:
        """The dash style of the median. Defaults to ``'Solid'``.

        Accepts one of the following values:

          * 'Dash',
          * 'DashDot',
          * 'Dot',
          * 'LongDash',
          * 'LongDashDot',
          * 'LongDashDotDot',
          * 'ShortDash',
          * 'ShortDashDot',
          * 'ShortDashDotDot',
          * 'ShortDot',
          * 'Solid'

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._median_dash_style

    @median_dash_style.setter
    def median_dash_style(self, value):
        if not value:
            self._median_dash_style = None
        else:
            value = validators.string(value)
            if value not in constants.SUPPORTED_DASH_STYLE_VALUES:
                raise errors.HighchartsValueError(f'median_dash_style expects a '
                                                  f' recognized value, but received: '
                                                  f'{value}')
            self._median_dash_style = value

    @property
    def median_width(self) -> Optional[int | float | Decimal]:
        """The pixel width of the median line. If :obj:`None <python:None>`, the
        :meth:`line_width <BoxPlotOptions.line_width>` is used. Defaults to ``2``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._median_width

    @median_width.setter
    def median_width(self, value):
        self._median_width = validators.numeric(value,
                                                allow_empty = True,
                                                minimum = 0)

    @property
    def stem_dash_style(self) -> Optional[str]:
        """The dash style of the :term:`stem`, the vertical line extending from the box to
        the whiskers. Defaults to ``'Solid'``.

        Accepts one of the following values:

          * 'Dash',
          * 'DashDot',
          * 'Dot',
          * 'LongDash',
          * 'LongDashDot',
          * 'LongDashDotDot',
          * 'ShortDash',
          * 'ShortDashDot',
          * 'ShortDashDotDot',
          * 'ShortDot',
          * 'Solid'

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._stem_dash_style

    @stem_dash_style.setter
    def stem_dash_style(self, value):
        if not value:
            self._stem_dash_style = None
        else:
            value = validators.string(value)
            if value not in constants.SUPPORTED_DASH_STYLE_VALUES:
                raise errors.HighchartsValueError(f'stem_dash_style expects a recognized'
                                                  f' value, but received: {value}')
            self._stem_dash_style = value

    @property
    def stem_width(self) -> Optional[int | float | Decimal]:
        """The pixel width of the stem line. If :obj:`None <python:None>`, the
        :meth:`line_width <BoxPlotOptions.line_width>` is used. Defaults to
        :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._stem_width

    @stem_width.setter
    def stem_width(self, value):
        self._stem_width = validators.numeric(value,
                                                allow_empty = True,
                                                minimum = 0)

    @property
    def whisker_color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the :term:`whiskers <whisker>`, the horizontal lines marking low
        and high values. When :obj:`None <python:None>`, the general series color is used.
        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern`, or
        :obj:`None <python:None>`
        """
        return self._whisker_color

    @whisker_color.setter
    def whisker_color(self, value):
        from highcharts import utility_functions
        self._whisker_color = utility_functions.validate_color(value)

    @property
    def whisker_dash_style(self) -> Optional[str]:
        """The dash style of the whiskers. Defaults to ``'Solid'``.

        Accepts one of the following values:

          * 'Dash',
          * 'DashDot',
          * 'Dot',
          * 'LongDash',
          * 'LongDashDot',
          * 'LongDashDotDot',
          * 'ShortDash',
          * 'ShortDashDot',
          * 'ShortDashDotDot',
          * 'ShortDot',
          * 'Solid'

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._whisker_dash_style

    @whisker_dash_style.setter
    def whisker_dash_style(self, value):
        if not value:
            self._whisker_dash_style = None
        else:
            value = validators.string(value)
            if value not in constants.SUPPORTED_DASH_STYLE_VALUES:
                raise errors.HighchartsValueError(f'whisker_dash_style expects a '
                                                  f'recognized value, but received: '
                                                  f'{value}')
            self._whisker_dash_style = value

    @property
    def whisker_length(self) -> Optional[str | int | float | Decimal]:
        """The length of the whiskers, the horizontal lines marking low and high values.
        It can be a numerical pixel value, or a percentage value of the box width. Set to
        ``0`` to disable whiskers entirely.

        Defaults to ``'50%'``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._whisker_length

    @whisker_length.setter
    def whisker_length(self, value):
        if value is None:
            self._whisker_length = None
        else:
            try:
                value = validators.string(value)
                if '%' not in value:
                    raise ValueError
            except ValueError:
                value = validators.numeric(value,
                                           allow_empty = True,
                                           minimum = 0)
            self._whisker_length = value

    @property
    def whisker_width(self) -> Optional[int | float | Decimal]:
        """The pixel width of the whisker line. If :obj:`None <python:None>`, the
        :meth:`line_width <BoxPlotOptions.line_width>` is used. Defaults to ``2``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._whisker_width

    @whisker_width.setter
    def whisker_width(self, value):
        self._whisker_width = validators.numeric(value,
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
            'fill_color': as_dict.pop('fillColor', None),
            'fill_opacity': as_dict.pop('fillOpacity', None),
            'find_nearest_point_by': as_dict.pop('findNearestPointBy', None),
            'get_extremes_for_all': as_dict.pop('getExtremesForAll', None),
            'linecap': as_dict.pop('linecap', None),
            'line_color': as_dict.pop('lineColor', None),
            'line_width': as_dict.pop('lineWidth', None),
            'negative_color': as_dict.pop('negativeColor', None),
            'negative_fill_color': as_dict.pop('negativeFillColor', None),
            'point_interval': as_dict.pop('pointInterval', None),
            'point_interval_unit': as_dict.pop('pointIntervalUnit', None),
            'point_placement': as_dict.pop('pointPlacement', None),
            'point_start': as_dict.pop('pointStart', None),
            'relative_x_value': as_dict.pop('relativeXValue', None),
            'shadow': as_dict.pop('shadow', None),
            'soft_threshold': as_dict.pop('softThreshold', None),
            'stacking': as_dict.pop('stacking', None),
            'step': as_dict.pop('step', None),
            'track_by_area': as_dict.pop('trackByArea', None),
            'zone_axis': as_dict.pop('zoneAxis', None),
            'zones': as_dict.pop('zones', None),

            'border_color': as_dict.pop('borderColor', None),
            'border_radius': as_dict.pop('borderRadius', None),
            'border_width': as_dict.pop('borderWidth', None),
            'center_in_category': as_dict.pop('centerInCategory', None),
            'color_by_point': as_dict.pop('colorByPoint', None),
            'depth': as_dict.pop('depth', None),
            'edge_color': as_dict.pop('edgeColor', None),
            'edge_width': as_dict.pop('edgeWidth', None),
            'grouping': as_dict.pop('grouping', None),
            'group_padding': as_dict.pop('groupPadding', None),
            'group_z_padding': as_dict.pop('groupZPadding', None),
            'max_point_width': as_dict.pop('maxPointWidth', None),
            'min_point_length': as_dict.pop('minPointLength', None),
            'point_padding': as_dict.pop('pointPadding', None),
            'point_range': as_dict.pop('pointRange', None),
            'point_width': as_dict.pop('pointWidth', None),

            'box_dash_style': as_dict.pop('boxDashStyle', None),
            'median_color': as_dict.pop('medianColor', None),
            'median_dash_style': as_dict.pop('medianDashStyle', None),
            'median_width': as_dict.pop('medianWidth', None),
            'stem_dash_style': as_dict.pop('stemDashStyle', None),
            'stem_width': as_dict.pop('stemWidth', None),
            'whisker_color': as_dict.pop('whiskerColor', None),
            'whisker_dash_style': as_dict.pop('whiskerDashStyle', None),
            'whisker_length': as_dict.pop('whiskerLength', None),
            'whisker_width': as_dict.pop('whiskerWidth', None)
        }

        return kwargs

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'boxDashStyle': self.box_dash_style,
            'medianColor': self.median_color,
            'medianDashStyle': self.median_dash_style,
            'medianWidth': self.median_width,
            'stemDashStyle': self.stem_dash_style,
            'stemWidth': self.stem_width,
            'whiskerColor': self.whisker_color,
            'whiskerDashStyle': self.whisker_dash_style,
            'whiskerLength': self.whisker_length,
            'whiskerWidth': self.whisker_width
        }
        parent_as_dict = super(self)._to_untrimmed_dict()

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class ErrorBarOptions(BoxPlotOptions):
    """General options to apply to all Error Bar series types.

    Error bars are a graphical representation of the variability of data and are used
    on graphs to indicate the error, or uncertainty in a reported measurement.

    .. figure:: _static/errorbar-example.png
      :alt: Error Bar Example Chart
      :align: center

    """
    pass

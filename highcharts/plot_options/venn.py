from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts.decorators import class_sensitive
from highcharts.plot_options.generic import GenericTypeOptions
from highcharts.utility_classes.clusters import ClusterOptions


class VennOptions(GenericTypeOptions):
    """General options to apply to all Venn series types.

    A Venn diagram displays all possible logical relations between a collection of
    different sets. The sets are represented by circles, and the relation between the
    sets are displayed by the overlap or lack of overlap between them. The venn
    diagram is a special case of Euler diagrams, which can also be displayed by this
    series type.

    .. tabs::

      .. tab:: Venn Diagram

        .. figure:: _static/venn-example.png
          :alt: Venn Example Chart
          :align: center

      .. tab:: Euler Diagram

        .. figure:: _static/venn-example-euler.png
          :alt: Euler Example Chart
          :align: center

    """

    def __init__(self, **kwargs):
        self._animation_limit = None
        self._color_axis = None
        self._color_index = None
        self._color_key = None
        self._crisp = None
        self._relative_x_value = False
        self._step = None

        self._border_dash_style = None

        self._brighten = None
        self._cluster = None

        self.animation_limit = kwargs.pop('animation_limit', None)
        self.color_axis = kwargs.pop('color_axis', None)
        self.color_index = kwargs.pop('color_index', None)
        self.color_key = kwargs.pop('color_key', None)
        self.crisp = kwargs.pop('crisp', None)
        self.relative_x_value = kwargs.pop('relative_x_value', None)
        self.step = kwargs.pop('step', None)

        self.border_dash_style = kwargs.pop('border_dash_style', None)
        self.brighten = kwargs.pop('brighten', None)
        self.cluster = kwargs.pop('cluster', None)

        super().__init__(**kwargs)

    @property
    def animation_limit(self) -> Optional[int | float | Decimal]:
        """For some series, there is a limit that shuts down initial animation by default
        when the total number of points in the chart is too high. Defaults to
        :obj:`None <python:None>`.

        For example, for a column chart and its derivatives, animation does not run if
        there is more than 250 points totally. To disable this cap, set
        ``animation_limit`` to ``float("inf")`` (which represents infinity).

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._animation_limit

    @animation_limit.setter
    def animation_limit(self, value):
        if value == float('inf'):
            self._animation_limit = float('inf')
        else:
            self._animation_limit = validators.numeric(value,
                                                       allow_empty = True,
                                                       minimum = 0)

    @property
    def border_dash_style(self) -> Optional[str]:
        """The dash style to apply to the border. Defaults to ``'solid'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._border_dash_style

    @border_dash_style.setter
    def border_dash_style(self, value):
        self._border_dash_style = validators.string(value, allow_empty = True)

    @property
    def brighten(self) -> Optional[int | float | Decimal]:
        """Defaults to ``0``. Factor by which to brighten the diagram.

        .. warning::

          This feature is not well documented, so this is merely a "guess" as to its
          functionality.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._brighten

    @brighten.setter
    def brighten(self, value):
        self._brighten = validators.numeric(value, allow_empty = True)

    @property
    def cluster(self) -> Optional[ClusterOptions]:
        """Options for marker clusters, the concept of sampling the data values into
        larger blocks in order to ease readability and increase performance of the
        JavaScript charts.

        .. warning::

          The marker clusters module does not work with ``boost`` and ``draggable-points``
          modules.

        .. note::

          The marker clusters feature requires the ``marker-clusters.js`` file to be
          loaded, found in the modules directory of the download package, or online at
          `code.highcharts.com/modules/marker-clusters.js <code.highcharts.com/modules/marker-clusters.js>`_.

        """
        return self._cluster

    @cluster.setter
    @class_sensitive(ClusterOptions)
    def cluster(self, value):
        self._cluster = value

    @property
    def color_axis(self) -> Optional[str | int | bool]:
        """When using dual or multiple color axes, this setting defines which
        :term:`color axis` the particular series is connected to. It refers to either the
        :meth:`ColorAxis.id` or the index of the axis in the :class:`ColorAxis` array,
        with ``0`` being the first. Set this option to ``False`` to prevent a series from
        connecting to the default color axis.

        Defaults to ``0``.

        :rtype: :obj:`None <python:None>` or :class:`str <python:str>` or
          :class:`int <python:int>` or :class:`bool <python:bool>`
        """
        return self._color_axis

    @color_axis.setter
    def color_axis(self, value):
        if value is None:
            self._color_axis = None
        elif value is False:
            self._color_axis = False
        else:
            try:
                self._color_axis = validators.string(value)
            except TypeError:
                self._color_axis = validators.integer(value,
                                                      minimum = 0)

    @property
    def color_index(self) -> Optional[int]:
        """When operating in :term:`styled mode`, a specific color index to use for the
        series, so that its graphic representations are given the class name
        ``highcharts-color-{n}``.

        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._color_index

    @color_index.setter
    def color_index(self, value):
        self._color_index = validators.integer(value,
                                               allow_empty = True,
                                               minimum = 0)

    @property
    def color_key(self) -> Optional[str]:
        """Determines what data value should be used to calculate point color if
        :meth:`AreaOptions.color_axis` is used.

        .. note::

          Requires to set ``min`` and ``max`` if some custom point property is used or if
          approximation for data grouping is set to ``'sum'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._color_key

    @color_key.setter
    def color_key(self, value):
        self._color_key = validators.string(value, allow_empty = True)

    @property
    def crisp(self) -> Optional[bool]:
        """If ``True``, each point or column edge is rounded to its nearest pixel in order
        to render sharp on screen. Defaults to ``True``.

        .. hint::

          In some cases, when there are a lot of densely packed columns, this leads to
          visible difference in column widths or distance between columns. In these cases,
          setting ``crisp`` to ``False`` may look better, even though each column is
          rendered blurry.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._crisp

    @crisp.setter
    def crisp(self, value):
        if value is None:
            self._crisp = None
        else:
            self._crisp = bool(value)

    @property
    def relative_x_value(self) -> Optional[bool]:
        """When ``True``, X values in the data set are relative to the current
        :meth:`point_start <AreaOptions.point_start>`,
        :meth:`point_interval <AreaOptions.point_interval>`, and
        :meth:`point_interval_unit <AreaOptions.point_interval_unit>` settings. This
        allows compression of the data for datasets with irregular X values. Defaults to
        ``False``.

        The real X values are computed on the formula ``f(x) = ax + b``, where ``a`` is
        the :meth:`point_interval <AreaOptions.point_interval>` (optionally with a time
        unit given by :meth:`point_interval_unit <AreaOptions.point_interval_unit>`), and
        ``b`` is the :meth:`point_start <AreaOptions.point_start>`.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._relative_x_value

    @relative_x_value.setter
    def relative_x_value(self, value):
        if value is None:
            self._relative_x_value = None
        else:
            self._relative_x_value = bool(value)

    @property
    def step(self) -> Optional[str]:
        """Whether to apply steps to the line. Defaults to :obj:`None <python:None>`.

        Possible values are:

          * :obj:`None <python:None>`
          * ``'left'``
          * ``'center'``
          * ``'right'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._step

    @step.setter
    def step(self, value):
        self._step = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        """Convenience method which returns the keyword arguments used to initialize the
        class from a Highcharts Javascript-compatible :class:`dict <python:dict>` object.

        :param as_dict: The HighCharts JS compatible :class:`dict <python:dict>`
          representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :returns: The keyword arguments that would be used to initialize an instance.
        :rtype: :class:`dict <python:dict>`

        """
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
            'sticky_tracking': as_dict.pop('stickyTracking', None),
            'threshold': as_dict.pop('threshold', None),
            'tooltip': as_dict.pop('tooltip', None),
            'turbo_threshold': as_dict.pop('turboThreshold', None),
            'visible': as_dict.pop('visible', None),

            'animation_limit': as_dict.pop('animationLimit', None),
            'color_axis': as_dict.pop('colorAxis', None),
            'color_index': as_dict.pop('colorIndex', None),
            'color_key': as_dict.pop('colorKey', None),
            'crisp': as_dict.pop('crisp', None),
            'relative_x_value': as_dict.pop('relativeXValue', None),
            'step': as_dict.pop('step', None),

            'border_dash_style': as_dict.pop('borderDashStyle', None),
            'brighten': as_dict.pop('brighten', None),
            'cluster': as_dict.pop('cluster', None)
        }

        return kwargs

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'animation_limit': self.animation_limit,
            'color_axis': self.color_axis,
            'color_index': self.color_index,
            'color_key': self.color_key,
            'crisp': self.crisp,
            'relative_x_value': self.relative_x_value,
            'step': self.step,

            'border_dash_style': self.border_dash_style,
            'brighten': self.brighten,
            'cluster': self.cluster
        }

        parent_as_dict = super()._to_untrimmed_dict() or {}
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed

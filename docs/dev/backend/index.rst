Flexopt
========

Flexopt repository contains application and libraries used in the process of
calculating flexibility offers by aggregators for a specific date. Once an
aggregator logs in, he selects buildings whose consumption he wants to
optimize according to the flexibility request acquired from Beyond platform.
Once the buildings and the period are selected, aggregator can submit that
data into Flexopt algorithm that returns offered flexibility in the requested
period and for the requested buildings. If the aggregator is satisfied with
the result, the result can be saved. Results that are saved can then be
accessed by Beyond platform for further analysis. On the other hand, when a
building manager logs in, he can see what optimizations are to be done on
his buildings.

Content
-------

.. toctree::
    :maxdepth: 1

    controller/index
    flexopt_algorithm/index
    models/index
    validator/index
    view/index
    common
    urls


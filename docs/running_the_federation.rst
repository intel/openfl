.. # Copyright (C) 2020-2021 Intel Corporation
.. # SPDX-License-Identifier: Apache-2.0

.. _running_the_federation:

**********************
Running the Federation
**********************

First make sure you've installed the software :ref:`using these instructions <install_initial_steps>`

.. figure:: images/openfl_flow.png

    100K foot view of OpenFL workflow
    
The high-level workflow is shown in the figure above. Note that once OpenFL is installed on all nodes of the federation and every member of the federation has a valid PKI certificate, all that is needed to run an instance of a federated workload is to distribute the workspace to all federation members and then run the command to start the node (e.g. :code:`fx aggregator start`/:code:`fx collaborator start`).

.. toctree::
   :maxdepth: 4

   running_the_federation.notebook
   running_the_federation.baremetal
   running_the_federation.docker
   running_the_federation.certificates
   running_the_federation.start_nodes.rst

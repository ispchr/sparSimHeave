# FSI_Buoy

## Basic Description and How to Run
This wave-structure interaction model replicates the movement of a heaving buoy (from McCormick's Ocean Engineering Mechanics) under the influence of regular water waves. The repository is meant to be run on OpenFOAM+ v1712. Just hit `sh Allrun` on your Linux terminal and all required pre-processors together with the two-phase solver should run sequently. The setup itself is quite demanding with a domain discretization of 10 cells per wave height near the free-surface region. Temporal discretization is defined by a Courant number restriction of 1. The total run-time was close to a full-day (24 hours), even though the case was run in parallel between 6 processors. Please feel free to relax the applied discretization if you want some quick results!

## The Setup
Regular waves (2nd order) are created at the boundaries using the Static Boundary Method (SBM). The cylindrical buoy is imported into the computational domain using the _snappyHexMesh_ pre-processor. Mesh morphing is used to topologically change the mesh influenced by the buoy's movement. The buoy's rigid movements are calculated with the help of the _sixDoFRigidBodyMotion_ solver, where the heave Degree of Freedom (DoF) has been activated. The _interFoam_ solver for multiphase and continuous flows is deployed in this model. No turbulance is accounted here (laminar simulation), but adding yours will definetely give you more valid results. I would recommend using the k-epsilon turbulence model.

## Post-Processig Scripts
Accompanying post-processing python scripts are also included to help you calculate and plot the buoy's movement and wave elevations at the different locations where the line samples are taken (have a look through the functions sub-dictionary of the controlDict, where the line samples are defined)

## Results
![UMagnitudeAt180](https://user-images.githubusercontent.com/55588269/134431923-abcb51bf-9b52-4fb4-82b4-e3172cab0718.png)
>Label: Magnitude of Velocity Field (U) at the 180th time step (only alpha.water=0.5 or simply the free-surface is visualized)

![heavePlotted](https://user-images.githubusercontent.com/55588269/134432256-8500b9eb-f2f2-4da5-9b18-b88ee8786a62.png)   
>Label: Simulated Heaving Motion

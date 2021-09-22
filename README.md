# FSI_Buoy

This wave-structure interaction model replicates the movement of a heaving buoy under the influence of regular water waves. The repository is meant to be run on OpenFOAM+ v1712. Regular waves (2nd order) are created at the boundaries using the Static Boundary Method (SBM). The cylindrical buoy is imported into the computational domain using the _snappyHexMesh_ utility pre-processor. Mesh morphing is used to adapt the mesh influenced by the buoy's movement. The buoy's rigid movements are calculated with the help of the _sixDoFRigidBodyMotion_ solver. The _interFoam_ solver for multiphase and continuous flows is deployed in this model. No turbulance model are accounted in this model (laminar simulation), but adding yours will definetely give you more valid results. 

![UMagnitudeAt180](https://user-images.githubusercontent.com/55588269/134431923-abcb51bf-9b52-4fb4-82b4-e3172cab0718.png)
Label: Magnitude of Velocity Field (U) at the 180th time step

![heavePlotted](https://user-images.githubusercontent.com/55588269/134432256-8500b9eb-f2f2-4da5-9b18-b88ee8786a62.png)
Label: Simulated Heaving Movement

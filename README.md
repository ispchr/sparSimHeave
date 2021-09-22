# FSI_Buoy

This wave-structure interaction model replicates the movement of a heaving buoy under the influence of regular water waves. The repository is meant to be run on OpenFOAM+ v1712. Regular waves (2nd order) are created at the boundaries using the Static Boundary Method (SBM). The cylindrical buoy is imported into the computational domain using the snappyHexMesh utility pre-processor. Mesh morphing is used to adapt the mesh influenced by the buoy's movement. The interFoam solver for multiphase and continuous flows is deployed in this model.

![UMagnitudeAt180](https://user-images.githubusercontent.com/55588269/134431923-abcb51bf-9b52-4fb4-82b4-e3172cab0718.png)

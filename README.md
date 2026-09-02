# Residual Topography of Back-Arc Basins

This repository contains the data and workflows used to extract residual topography within back-arc basins and calculate slab dip.

## Repository Contents

The repository includes:

* **Five residual-topography NetCDF files** (`.nc`)
* **Basin polygons** defining the back-arc basins analysed in this study
* **Workflows** for:

  * extracting residual topography within back-arc basins
  * calculating slab dip
* **Subduction zones** folder containing subduction zones associated with or located near the back-arc basins analysed in this study

## Residual Topography Data

The residual-topography files are provided in **NetCDF (`.nc`) format**. These files contain residual topography calculated using different crustal-thickness models and age–depth relationships.

### Crustal-Thickness Models

Three crustal-thickness models are used for the crustal-thickness correction:

* **CRUST1.0** — Laske et al. (2012)
* **ECM1** — Mooney et al. (2023)
* **LithoRef18** — Afonso et al. (2019)

### Age–Depth Relationships

Three age–depth relationships are applied:

* **Richards et al. (2018)**
* **GDH1** — Stein & Stein (1992)
* **Crosby & McKenzie (2009)**

## Workflows

The repository provides workflows for:

1. Extracting residual-topography values within each back-arc basin.
2. Calculating representative residual topography for each basin.
3. Extracting trench-normal slab profiles.
4. Calculating representative slab dip for each subduction zone or trench segment.

## Subduction Zones

The `subduction_zones/` folder contains the subduction-zone geometries associated with or located near the back-arc basins analysed in this study.

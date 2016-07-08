## TRON 2.0

### Structure

- [`main.yaml`](scene/main.yaml): Mostly a HUB that mix the `sources`, `layers` and the common `styles` together with some `cameras` and `lights` definitions. Here we put high level settings.
 - [`layers/`](scene/layers): The following rules apply
    1. Each layer have individual `.yaml` file (`water.yaml`,`earth.yaml`, etc) where each layer is define and fitered. 
    2. Each filter element of a layer is named in a consisten way following this structure: `[layer]-[filtered_element_layer]`. If there are subsections the filtered "parent" also is mention so it's posible to keep track of the hierarchical logical dependencies: `[layer]-[filtered_element_layer]-[filtered_subelement_layer]`. The same happen if a subelement is filtered. **Note:** as a convention we *separate names* with a `-` (dash), while we reserve the `_` to *separate words* of a name like: `water-swimming_pool`. 
    3. Unless the filtered layer introduce or use a custom layer that diferentiates from the parent style, and if that style extend from the `polygons` or `lines` base style will use a **custom style that shares the same name**, each style is initialited in the same `.yaml` file. Specifing the `base` style (`polygon` or `lines`) and, in case it needs an array of styles to `mix`.
    4. In the case to styles respond to the same filter but differ in the base style 3 extra letters are attach to the end of the name pointing if it is `-ply` for `polygons` or `-lns` for `lines`. So a same filter layer can point to two different drawing styles. For example: `building-ply` and `building-lns`.  

 - ['styles/'](scene/styles): Thin on this folder as the **blocks** of trons. Styles that can be reuse are defined here and mixed on the `layers/[layer_name].yaml` files.  

### Resources

- [Inspiration Pintboard](https://www.pinterest.com/patriciogonzv/tron-20/)

### Authors

- [Geraldine Sarmiento](https://twitter.com/sensescape)

- [Patricio Gonzalez Vivo](https://twitter.com/patriciogv)
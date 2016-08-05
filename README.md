## TRON 2.0

## Try new things

If you want to try something new with Tron 2.0 style:

1. [Click here to open Tron in TangramPlay](https://mapzen.com/tangram/play/?scene=https%3A%2F%2Fgist.githubusercontent.com%2Fanonymous%2F1ead441ee35e5a18741437dea7916f33%2Fraw%2F547146cf5a975a8b4e1eba84eba77df9b8a625b5%2Fscene.yaml#8/40.574/-74.051)

2. Then, copy the content of the `.yaml` file you want to edit with `Cmd-a`, copy it with `Cmd-c` and then paste it to TangramPlay with `Cmd-v`.

3. Edit.

4. Once you finish you can download it or copy it back to your local file, but **remember** to take out the first line `import`.

### Structure

- [`tron.yaml`](scene/tron.yaml): Mostly a HUB that mix the `sources`, `layers` and the common `styles` together with some `cameras` and `lights` definitions. Here we put high level settings.
 - [`layers/`](scene/layers): The following rules apply
    1. Each layer have individual `.yaml` file (`water.yaml`,`earth.yaml`, etc) where each layer is define and fitered. 
    2. Unless the filtered layer introduce or use a custom layer that diferentiates from the parent style, and if that style extend from the `polygons` or `lines` base style will use a **custom style that shares the same name**, each style is initialited in the same `.yaml` file. Specifing the `base` style (`polygon` or `lines`) and, in case it needs an array of styles to `mix`. For namig the style if it's posible, keep track of the hierarchical logical dependencies: `[layer]-[filtered_element_layer]-[filtered_subelement_layer]`. **Note:** as a convention we *separate names* with a `-` (dash), while we reserve the `_` to *separate words* of a name like: `water-swimming_pool`. 
    3. In the case to styles respond to the same filter but differ in the base style 3 extra letters are attach to the end of the name pointing if it is `-ply` for `polygons` or `-lns` for `lines`. So a same filter layer can point to two different drawing styles. For example: `building-ply` and `building-lns`.  
 - ['styles/'](scene/styles): Things on this folder as the **blocks** of trons. Styles that can be reuse are defined here and mixed on the `layers/[layer_name].yaml` files. This abstract styles, mean to be reuse, are named acording to if they are apply to `lines` or `polygons` followed by the name of the styling. For ex: `lines-glow` or `polygons-dots`. If the defined styles can be apply to both `lines` or `polygons` they should be under `commons.yaml` with out any word at the begining.  

### Resources

- [Inspiration Pintboard](https://www.pinterest.com/patriciogonzv/tron-20/)

#### Some shaders prototypes that compose this map:

[![](http://thebookofshaders.com/log/160726003844.png) Generative Tron Palette](http://player.thebookofshaders.com/?log=160726003844)
[![](http://thebookofshaders.com/log/160726010850.png) Glow lines ](http://player.thebookofshaders.com/?log=160726010850)
[![](http://thebookofshaders.com/log/160706191515.png) Grid animation](http://player.thebookofshaders.com/?log=160706191515)
[![](http://thebookofshaders.com/log/160705205611.png) Grid animation](http://player.thebookofshaders.com/?log=160705205611)
[![](http://thebookofshaders.com/log/160229221706.png) Stripes](http://player.thebookofshaders.com/?log=160229221706)
[![](http://thebookofshaders.com/log/160705204919.png) Stripes animation](http://player.thebookofshaders.com/?log=160705204919)
[![](http://thebookofshaders.com/log/160313020334.png) Simplex Grid animation](http://player.thebookofshaders.com/?log=160313020334)
[![](http://thebookofshaders.com/log/160621211003.png) Dots pattern](http://player.thebookofshaders.com/?log=160621211003)
[![](http://thebookofshaders.com/log/160622150357.png) Mosaic-dots transition](http://player.thebookofshaders.com/?log=160622150357)
[![](http://thebookofshaders.com/log/160621210032.png) Stripes](http://player.thebookofshaders.com/?log=160621210032)
[![](http://thebookofshaders.com/log/160621170831.png) Stripes-char transition](http://player.thebookofshaders.com/?log=160621170831)
[![](http://thebookofshaders.com/log/160626213924.png) Contours](http://player.thebookofshaders.com/?log=160626213924)
[![](http://thebookofshaders.com/log/160705083231.png) Hill Shading](http://player.thebookofshaders.com/?log=160705083231)
[![](http://thebookofshaders.com/log/160707203604.png) Buildings window](http://player.thebookofshaders.com/?log=160707203604)
[![](http://thebookofshaders.com/log/160805190306.png) Tron Icons](http://player.thebookofshaders.com/?log=160805190306)

### Authors

- [Geraldine Sarmiento](https://twitter.com/sensescape)

- [Patricio Gonzalez Vivo](https://twitter.com/patriciogv)
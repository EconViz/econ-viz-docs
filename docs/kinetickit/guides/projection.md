---
seo_title: "Camera geometry and projection"
---

# Camera geometry and projection

<span id="sec-kinetic-projection"></span>

## View and projection matrices

KineticKit projects 3D scenes through a view matrix $V$ and projection matrix $P$. A world point $p=(x,y,z,1)^T$ becomes clip coordinates

$$
c = P V p.
$$

Perspective division gives normalised device coordinates $n=(c_x/c_w,c_y/c_w,c_z/c_w)$, then a viewport of width $W$ and height $H$ maps

$$
x_{\text{px}}=(n_x+1) W/2, \quad y_{\text{px}}=(1-n_y) H/2.
$$

The sign change puts the SVG and raster origin at the top left.

## Visibility and ordering

View depth is $d=-z_{\text{view}}$. Geometry is retained when `near` $\le d \le$ `far`. Projected primitives are sorted from large depth to small depth, using a stable painter's algorithm so equal-depth scene order is deterministic.

## Surface normals and shading

For a triangle $(p_0,p_1,p_2)$, the unnormalised normal is

$$
n=(p_1-p_0) \times (p_2-p_0).
$$

Degenerate faces are removed. One-sided faces are culled by the sign of $n \cdot v$, where $v$ points toward the eye. Flat diffuse and specular terms are computed per face before colours reach the output renderer.

<!-- api: agora.kinetickit.guides_projection_1 -->

Defines view and projection matrices for perspective or orthographic output.

<!-- api: agora.kinetickit.guides_projection_2 -->

Stores a regular height field and converts its grid cells into consistently ordered projected faces.

<!-- api: agora.kinetickit.guides_projection_3 -->

Stores indexed 3D geometry whose faces are clipped, culled, shaded, and depth-sorted before output.

## Output invariance

[A 3D surface projected and depth-sorted by KineticKit's vector renderer](scenes-motion.md#fig-kinetic-surface) therefore has the same geometry in animated SVG, representative PNG, and GIF frames.

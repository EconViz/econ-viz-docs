---
seo_title: "相机几何与投影"
---

# 相机几何与投影

<span id="sec-kinetic-projection"></span>

## 查看与投影矩阵

场景中的 3D 点先以世界坐标表示。写成齐次坐标 $p_h = (x, y, z, 1)^T$ 后，依序套用查看矩阵 $V$ 与投影矩阵 $P$：$c = P V p_h$。透视除法得到 $n = (c_x / c_w, c_y / c_w, c_z / c_w)$，再映射到宽 $W$、高 $H$ 的画布：

$$
x_{\text{px}} = (n_x + 1) W / 2, \quad y_{\text{px}} = (1 - n_y) H / 2.
$$

纵坐标的反号让 SVG 与位图输出都采左上原点。

## 可见范围与深度排序

查看坐标中的深度为 $d = -z_{\text{view}}$，只有位于 `near` 与 `far` 之间的几何会留下。绘图元素（图元）由远到近稳定排序，相同深度保留场景顺序。

## 法矢量与着色

三角形法矢量为 $n = (p_1 - p_0) \times (p_2 - p_0)$。面积为零的三角形会移除；只显示正面的表面以 $n \cdot v$ 判断背面；漫反射与镜面项在输出前逐面计算。

<!-- api: kinetickit.guides_projection_1 -->

为透视或正交输出创建查看矩阵与投影矩阵。

<!-- api: kinetickit.guides_projection_2 -->

保存规则高度场，并把网格单元转成顺序一致的投影面。

<!-- api: kinetickit.guides_projection_3 -->

保存索引式 3D 几何；输出前会裁切、背面剔除、着色并依深度排序各个面。

## 输出格式的一致性

因此 [由 KineticKit 矢量绘图端投影并排序深度的 3D 曲面](scenes-motion.md#fig-kinetic-surface) 在动态 SVG、代表 PNG 与 GIF 帧中的几何一致。

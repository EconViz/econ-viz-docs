---
seo_title: "插补与座标变换"
---

# 插补与座标变换

<span id="sec-kinetic-interpolation"></span>

## 纯量、矢量、颜色与离散值

实数使用保留精确端点的线性插补 $L(a, b, u) = (1 - u) a + u b$；矢量与颜色逐分量套用，离散值则在指定门槛切换。

## 角度与仿射变换

角度采最短有号差

$$
\Delta=((b-a+\pi) \mod 2\pi)-\pi, \quad \theta(u)=a+u \Delta.
$$

2D 变换把平移、旋转、缩放与剪切组成 $3 \times 3$ 齐次矩阵。矩阵乘法的次序有意义，先平移再旋转并不等于先旋转再平移。

## 四元数旋转

单位轴 $v$ 与角度 $\theta$ 转成 $q=(\cos(\theta/2),v \sin(\theta/2))$。若 $q_0 \cdot q_1<0$，先反转 $q_1$ 以走短弧。令 $\theta=arccos(q_0 \cdot q_1)$，则

$$
\text{slerp}(q_0,q_1,u)=(\sin((1-u)\theta)/\sin \theta) q_0+(\sin(u \theta)/\sin \theta) q_1.
$$

两端几乎平行时改用范式线性插补，避免数值不稳定。

## 几何值与验证

<!-- api: kinetickit.guides_interpolation_transforms_1 -->

用于 3D 旋转的单位四元数；创建时会验证并范式有限、非零的分量。

<!-- api: kinetickit.guides_interpolation_transforms_2 -->

不可变的 2D 仿射变换，组合平移、旋转、缩放与剪切。

<!-- api: kinetickit.guides_interpolation_transforms_3 -->

不可变的 3D 齐次变换，用于平移、旋转、缩放与变换组合。

## 自订插补器

自订属性类型可向登录表（registry）注册插补器。KineticKit 在编译动作时解析类型与插补器；缺少实作会在输出任何帧之前失败。

---
seo_title: "帧采样与编码"
---

# 帧采样与编码

<span id="sec-kinetic-sampling"></span>

## 固定帧率的采样时间

动画长度 $D$、整数帧率 $f$ 时，`FixedFPS` 选择

$$
N = \max(2, \left\lfloor D f + 1 / 2 \right\rfloor)
$$

个帧，并包含两端：

$$
t_i = D i / (N - 1), \quad i = 0, ..., N - 1.
$$

最后一个时间直接指定为 $D$，不累积浮点误差。

## 自行指定采样时间

<!-- api: kinetickit.guides_sampling_encoding_1 -->

依指定的整数帧率，产生等距且包含首末端点的采样时间。

<!-- api: kinetickit.guides_sampling_encoding_2 -->

验证并保存动画范围内不递减的自定义采样时间。

<!-- api: kinetickit.guides_sampling_encoding_3 -->

一个采样后的场景，以及对应的时间、持续时间与帧编号。

## GIF 的百分之一秒

GIF 以百分之一秒保存延迟。帧率为 $f$ 时，KineticKit 由累积边界分配整数延迟：

$$
d_i = round((i + 1) 100 / f) - round(i 100 / f).
$$

当 $100 / f$ 不是整数时，相邻延迟会交替，但总漂移有界；逐帧各自四舍五入做不到这点。

## 串流输出与可重现性

GIF 写入器每次只量化并写出一个帧，因此内存不随片长增加。SVG 保存解析式动作；HTML 保存场景、时间轴、控制项与无障碍数据。每个导出器都会返回输出清单，说明格式、尺寸、长度、帧数与替代内容。

## 端点一致性

!!! abstract "命题 · 端点一致性"

    所有含端点的调度器，其首末场景都分别等于 `Animation.sample(0)` 与 `Animation.sample(D)`。

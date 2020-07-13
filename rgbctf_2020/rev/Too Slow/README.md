# Too Slow

Source: [a.out](./a.out)

Reading the decompilation, one function stands out:

```c
uint32_t getKey(void)
{
    uint32_t var_8h;
    uint32_t var_4h;

    var_8h = 0;
    while (var_8h < 0x265d1d23) {
        var_4h = var_8h;
        while (var_4h != 1) {
            if ((var_4h & 1) == 0) {
                var_4h = (int32_t)var_4h / 2;
            } else {
                var_4h = var_4h * 3 + 1;
            }
        }
        var_8h = var_8h + 1;
    }
    return var_8h;
}
```

This function is just returning `0x265d1d23` plus time wasting, so patch `var_8h`'s value to `0x265d1d23`. Running the [patched binary](./a.out_patched) will produce the flag.

Flag: rgbCTF{pr3d1ct4bl3_k3y_n33d5_no_w41t_cab79d}

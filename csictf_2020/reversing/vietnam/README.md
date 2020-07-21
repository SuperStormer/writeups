# Vietnam

Source: [vietnam](./vietnam)

Reversing reveals some brainfuck-like esolang that we need to use to produce `HELLO\n`. We notice that `,` is input one char and `.` is output one char, so chaining them produces our payload: `,.,.,.,.,.,.`.

Flag: `csictf{l00k_4t_th3_t0w3rs_0f_h4n01}`

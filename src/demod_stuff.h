#pragma once
#include "fm_process.h"

#ifdef _MSC_VER
double log2(double n);
#endif

void rotate_90(unsigned char *buf, uint32_t len);
void low_pass(struct demod_state *d);
int low_pass_simple(int16_t *signal2, int len, int step);
void low_pass_real(struct demod_state *s);
void fifth_order(int16_t *data, int length, int16_t *hist);
void generic_fir(int16_t *data, int length, int *fir, int16_t *hist);
void multiply(int ar, int aj, int br, int bj, int *cr, int *cj);
int polar_discriminant(int ar, int aj, int br, int bj);
int fast_atan2(int y, int x);
int polar_disc_fast(int ar, int aj, int br, int bj);
int atan_lut_init(void);
int polar_disc_lut(int ar, int aj, int br, int bj);
void fm_demod(struct demod_state *fm);
void am_demod(struct demod_state *fm);
void usb_demod(struct demod_state *fm);
void lsb_demod(struct demod_state *fm);
void raw_demod(struct demod_state *fm);
void deemph_filter(struct demod_state *fm);
void dc_block_filter(struct demod_state *fm);
int mad(int16_t *samples, int len, int step);
int rms(int16_t *samples, int len, int step);
void arbitrary_upsample(int16_t *buf1, int16_t *buf2, int len1, int len2);
void arbitrary_downsample(int16_t *buf1, int16_t *buf2, int len1, int len2);
void arbitrary_resample(int16_t *buf1, int16_t *buf2, int len1, int len2);
void full_demod(struct demod_state *d);

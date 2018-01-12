#include <assert.h>
#include <limits.h>
#include <stdio.h>
unsigned long euler_totient_function(unsigned long n) {
  /*
      r = resulting integer
      n = positive integer
      p = prime

   */
  assert(n < ULONG_MAX);

  unsigned long r = n;
  unsigned long p = 2;
  while (p * p <= n) {
    if (n % p == 0) {
      n /= p;
      r *= (1.0 - (1.0 / n));
    }
    p++;
  }
  if (n > 1) {
    r *= (1.0 - (1.0 / n));
  }

  return (unsigned long)r;
}


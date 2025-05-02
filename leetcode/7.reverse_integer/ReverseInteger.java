class ReverseInteger {
  public static void main(String[] args) {
    int x = reverse4(-2147483648);
    // int x = reverse3(-1563847412);
    System.out.println(x);

  }

  public static int reverse(int x) {
    int newNumber = x % 10;
    int limit;
    x = x / 10;
    if (x < 0) {
      limit = (int) Math.pow(2, 31) * -1;
    } else {
      limit = (int) Math.pow(2, 31) - 1;
    }
    long possibleNewNumber;
    while (x != 0) {
      if (x < 0) {
        possibleNewNumber = (long) newNumber * 10 - Math.abs((x % 10));
        if (possibleNewNumber < limit) {
          return 0;
        }
      } else {
        possibleNewNumber = (long) newNumber * 10 + (x % 10);
        if (possibleNewNumber > limit) {
          return 0;
        }
      }

      newNumber = (int) possibleNewNumber;
      x = x / 10;
    }
    return newNumber;

  }

  public static int reverse3(int x) {
    long rev = 0;
    int sign = 1;
    if (x < 0) {
      sign = -1;
      x = x * -1;
    }
    while (x != 0) {
      rev = rev * 10 + (x % 10);
      x = x / 10;
    }
    if (sign == 1 && rev > (1L << 31) - 1) {
      return 0;
    } else if (sign == -1 && rev > (1L << 31)) {
      return 0;
    }
    return (int) rev * sign;
  }

  public static int reverse2(int x) {
    long rev = 0;
    while (x != 0) {
      rev = rev * 10 + (x % 10);
      x = x / 10;
    }
    if (rev > 0 && rev > (1L << 31) - 1) {
      return 0;
    } else if (rev < 0 && rev < (1L << 31)) {
      return 0;
    }
    return (int) rev;
  }

  public static int reverse4(int x) {
    int sign = 1;
    if (x < 0) {
      sign = -1;
      x = -x;
    }

    long val = 0;

    while (x > 0) {
      int rem = x % 10;
      x = x / 10;
      val = val * 10 + rem;
    }

    // If reversed value exceeds 2^31, return 0
    if (val > (1L << 31) - 1)
      return 0;

    return (int) (sign * val);
  }
}

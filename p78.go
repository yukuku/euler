package main

var jw = make([][80000]int32, 80000)

func c(n, m int32) int32 {
	if n == 0 || n == 1 || m == 1 {
		return 1
	}
	if m > n {
		return c(n, n)
	}
	if jw[n][m] != 0 {
		return jw[n][m]
	}
	res := c(n-m, m) + c(n, m-1)
	res %= 1000000
	jw[n][m] = res
	return res
}

func main() {
	for n := int32(1); n < 80000; n++ {
		println(n)
		if c(n, n) == 0 {
			println(n)
			break
		}
	}
}

// --- Part Two ---
//
// Everyone will starve if you only plant such a small number of seeds.
// Re-reading the almanac, it looks like the seeds: line actually describes
// ranges of seed numbers.
//
// The values on the initial seeds: line come in pairs. Within each pair, the
// first value is the start of the range and the second value is the length of
// the range. So, in the first line of the example above:
//
// seeds: 79 14 55 13
//
// This line describes two ranges of seed numbers to be planted in the garden.
// The first range starts with seed number 79 and contains 14 values: 79, 80,
// ..., 91, 92. The second range starts with seed number 55 and contains 13
// values: 55, 56, ..., 66, 67.
//
// Now, rather than considering four seed numbers, you need to consider a total
// of 27 seed numbers.
//
// In the above example, the lowest location number can be obtained from seed
// number 82, which corresponds to soil 84, fertilizer 84, water 84, light 77,
// temperature 45, humidity 46, and location 46. So, the lowest location number
// is 46.
//
// Consider all of the initial seed numbers listed in the ranges on the first
// line of the almanac. What is the lowest location number that corresponds to
// any of the initial seed numbers?

package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"slices"
	"strconv"
	"strings"
	"sync"
	"time"
	"unicode"
)

func do_range(worker, start, length int, maps map[int][][]int, msg chan<- int) {
	p := fmt.Println

	p("thread", worker, "started\tstart:", start, "\tlength:", length)

	location_no := -1

	time_start := time.Now()
	first_start := time.Now()

	for seed := start; seed < start+length; seed++ {
		found_dest := false

		src := seed

		for m := 1; m <= len(maps); m++ {
			found_dest = false

			for a := range maps[m] {
				map_line := maps[m][a]

				if src >= map_line[1] && src < map_line[1]+map_line[2] {
					destx := map_line[0] + (src - map_line[1])
					found_dest = true
					src = destx
					break
				}

			}

			if found_dest {
				continue
			}
		}

		if location_no == -1 {
			location_no = src
		} else {
			if location_no > src {
				location_no = src
			}
		}

		time_diff := time.Now().Sub(time_start)
		if time_diff.Seconds() > 2 {
			completed := float32(float32(seed-start)/float32(length)) * 100

			time_since_start := time.Now().Sub(first_start)
			p("worker:", worker, "\ttime since started:", time_since_start, "\t% completed:", math.Round(float64(completed)))
			time_start = time.Now()
		}
	}

	p("thread", worker, "out!")
	msg <- location_no
}

func main() {
	p := fmt.Println
	// get seed ranges
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	one := scanner.Text()
	x := strings.Split(one, ": ")
	seeds_str := strings.Split(x[1], " ")
	seeds := []int{}
	for _, i := range seeds_str {
		j, _ := strconv.Atoi(i)
		seeds = append(seeds, j)
	}
	fmt.Println(seeds)

	// get maps
	maps := make(map[int][][]int)
	map_number := 0

	for scanner.Scan() {
		line := scanner.Text()

		if line == "" {
			continue
		}

		if unicode.IsLetter(rune(line[0])) {
			map_number++
			maps[map_number] = [][]int{}
		}

		if unicode.IsNumber(rune(line[0])) {
			numbers := strings.Fields(line)
			numbers_int := []int{}
			for _, i := range numbers {
				j, _ := strconv.Atoi(i)
				numbers_int = append(numbers_int, j)
			}
			maps[map_number] = append(maps[map_number], numbers_int)

		}
	}

	var wg sync.WaitGroup

	msg := make(chan int, len(seeds))
	workers := 0
	final_seeds := []int{}

	for seed_range := 0; seed_range < len(seeds); seed_range += 2 {
		wg.Add(1)
		workers++
		seed_range := seed_range
		go func() {
			defer wg.Done()
			do_range(seed_range, seeds[seed_range], seeds[seed_range+1], maps, msg)
		}()
	}

	wg.Wait()

	for i := 1; i <= workers; i++ {
		final_seeds = append(final_seeds, <-msg)
	}

	p(final_seeds)
	p(slices.Min(final_seeds))
}

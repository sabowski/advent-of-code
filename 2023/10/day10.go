// --- Day 10: Pipe Maze ---
//
// You use the hang glider to ride the hot air from Desert Island all the way
// up to the floating metal island. This island is surprisingly cold and there
// definitely aren't any thermals to glide on, so you leave your hang glider
// behind.
//
// You wander around for a while, but you don't find any people or animals.
// However, you do occasionally find signposts labeled "Hot Springs" pointing
// in a seemingly consistent direction; maybe you can find someone at the hot
// springs and ask them where the desert-machine parts are made.
//
// The landscape here is alien; even the flowers and trees are made of metal.
// As you stop to admire some metal grass, you notice something metallic scurry
// away in your peripheral vision and jump into a big pipe! It didn't look like
// any animal you've ever seen; if you want a better look, you'll need to get
// ahead of it.
//
// Scanning the area, you discover that the entire field you're standing on is
// densely packed with pipes; it was hard to tell at first because they're the
// same metallic silver color as the "ground". You make a quick sketch of all
// of the surface pipes you can see (your puzzle input).
//
// The pipes are arranged in a two-dimensional grid of tiles:
//
//   - | is a vertical pipe connecting north and south.
//   - - is a horizontal pipe connecting east and west.
//   - L is a 90-degree bend connecting north and east.
//   - J is a 90-degree bend connecting north and west.
//   - 7 is a 90-degree bend connecting south and west.
//   - F is a 90-degree bend connecting south and east.
//   - . is ground; there is no pipe in this tile.
//   - S is the starting position of the animal; there is a pipe on this tile,
//     but your sketch doesn't show what shape the pipe has.
//
// Based on the acoustics of the animal's scurrying, you're confident the pipe
// that contains the animal is one large, continuous loop.
//
// For example, here is a square loop of pipe:
//
// .....
// .F-7.
// .|.|.
// .L-J.
// .....
//
// If the animal had entered this loop in the northwest corner, the sketch
// would instead look like this:
//
// .....
// .S-7.
// .|.|.
// .L-J.
// .....
//
// In the above diagram, the S tile is still a 90-degree F bend: you can tell
// because of how the adjacent pipes connect to it.
//
// Unfortunately, there are also many pipes that aren't connected to the loop!
// This sketch shows the same loop as above:
//
// -L|F7
// 7S-7|
// L|7||
// -L-J|
// L|-JF
//
// In the above diagram, you can still figure out which pipes form the main
// loop: they're the ones connected to S, pipes those pipes connect to, pipes
// those pipes connect to, and so on. Every pipe in the main loop connects to
// its two neighbors (including S, which will have exactly two pipes connecting
// to it, and which is assumed to connect back to those two pipes).
//
// Here is a sketch that contains a slightly more complex main loop:
//
// ..F7.
// .FJ|.
// SJ.L7
// |F--J
// LJ...
//
// Here's the same example sketch with the extra, non-main-loop pipe tiles also
// shown:
//
// 7-F7-
// .FJ|7
// SJLL7
// |F--J
// LJ.LJ
//
// If you want to get out ahead of the animal, you should find the tile in the
// loop that is farthest from the starting position. Because the animal is in
// the pipe, it doesn't make sense to measure this by direct distance. Instead,
// you need to find the tile that would take the longest number of steps along
// the loop to reach from the starting point - regardless of which way around
// the loop the animal went.
//
// In the first example with the square loop:
//
// .....
// .S-7.
// .|.|.
// .L-J.
// .....
//
// You can count the distance each tile in the loop is from the starting point
// like this:
//
// .....
// .012.
// .1.3.
// .234.
// .....
//
// In this example, the farthest point from the start is 4 steps away.
//
// Here's the more complex loop again:
//
// ..F7.
// .FJ|.
// SJ.L7
// |F--J
// LJ...
//
// Here are the distances for each tile on that loop:
//
// ..45.
// .236.
// 01.78
// 14567
// 23...
//
// Find the single giant loop starting at S. How many steps along the loop does
// it take to get from the starting position to the point farthest from the
// starting position?
//
// --- Part Two ---
//
// You quickly reach the farthest point of the loop, but the animal never
// emerges. Maybe its nest is within the area enclosed by the loop?
//
// To determine whether it's even worth taking the time to search for such a
// nest, you should calculate how many tiles are contained within the loop. For
// example:
//
// ...........
// .S-------7.
// .|F-----7|.
// .||.....||.
// .||.....||.
// .|L-7.F-J|.
// .|..|.|..|.
// .L--J.L--J.
// ...........
//
// The above loop encloses merely four tiles - the two pairs of . in the
// southwest and southeast (marked I below). The middle . tiles (marked O
// below) are not in the loop. Here is the same loop again with those regions
// marked:
//
// ...........
// .S-------7.
// .|F-----7|.
// .||OOOOO||.
// .||OOOOO||.
// .|L-7OF-J|.
// .|II|O|II|.
// .L--JOL--J.
// .....O.....
//
// In fact, there doesn't even need to be a full tile path to the outside for
// tiles to count as outside the loop - squeezing between pipes is also
// allowed! Here, I is still within the loop and O is still outside the loop:
//
// ..........
// .S------7.
// .|F----7|.
// .||OOOO||.
// .||OOOO||.
// .|L-7F-J|.
// .|II||II|.
// .L--JL--J.
// ..........
//
// In both of the above examples, 4 tiles are enclosed by the loop.
//
// Here's a larger example:
//
// .F----7F7F7F7F-7....
// .|F--7||||||||FJ....
// .||.FJ||||||||L7....
// FJL7L7LJLJ||LJ.L-7..
// L--J.L7...LJS7F-7L7.
// ....F-J..F7FJ|L7L7L7
// ....L7.F7||L7|.L7L7|
// .....|FJLJ|FJ|F7|.LJ
// ....FJL-7.||.||||...
// ....L---J.LJ.LJLJ...
//
// The above sketch has many random bits of ground, some of which are in the
// loop (I) and some of which are outside it (O):
//
// OF----7F7F7F7F-7OOOO
// O|F--7||||||||FJOOOO
// O||OFJ||||||||L7OOOO
// FJL7L7LJLJ||LJIL-7OO
// L--JOL7IIILJS7F-7L7O
// OOOOF-JIIF7FJ|L7L7L7
// OOOOL7IF7||L7|IL7L7|
// OOOOO|FJLJ|FJ|F7|OLJ
// OOOOFJL-7O||O||||OOO
// OOOOL---JOLJOLJLJOOO
//
// In this larger example, 8 tiles are enclosed by the loop.
//
// Any tile that isn't part of the main loop can count as being enclosed by the
// loop. Here's another example with many bits of junk pipe lying around that
// aren't connected to the main loop at all:
//
// FF7FSF7F7F7F7F7F---7
// L|LJ||||||||||||F--J
// FL-7LJLJ||||||LJL-77
// F--JF--7||LJLJ7F7FJ-
// L---JF-JLJ.||-FJLJJ7
// |F|F-JF---7F7-L7L|7|
// |FFJF7L7F-JF7|JL---7
// 7-L-JL7||F7|L7F-7F7|
// L.L7LFJ|||||FJL7||LJ
// L7JLJL-JLJLJL--JLJ.L
//
// Here are just the tiles that are enclosed by the loop marked with I:
//
// FF7FSF7F7F7F7F7F---7
// L|LJ||||||||||||F--J
// FL-7LJLJ||||||LJL-77
// F--JF--7||LJLJIF7FJ-
// L---JF-JLJIIIIFJLJJ7
// |F|F-JF---7IIIL7L|7|
// |FFJF7L7F-JF7IIL---7
// 7-L-JL7||F7|L7F-7F7|
// L.L7LFJ|||||FJL7||LJ
// L7JLJL-JLJLJL--JLJ.L
//
// In this last example, 10 tiles are enclosed by the loop.
//
// Figure out whether you have time to search for the nest by calculating the
// area within the loop. How many tiles are enclosed by the loop?

package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"reflect"
	"regexp"
	"strings"
)

func load_data(maze *[]string) {
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		*maze = append(*maze, scanner.Text())
	}
}

func find_start(maze *[]string) ([2]int, error) {
	for line := range *maze {
		start := strings.Index((*maze)[line], "S")
		if start != -1 {
			return [2]int{line, start}, nil
		}
	}

	return [2]int{}, errors.New("no match found")
}

func find_adjacent(maze *[]string, coords [2]int) [][2]int {
	next := [][2]int{}
	current_symbol := string((*maze)[coords[0]][coords[1]])

	look_above, _ := regexp.MatchString(`[S|LJ]`, current_symbol)
	if coords[0] > 0 && look_above {
		match, _ := regexp.MatchString(`[F|7]`, string((*maze)[coords[0]-1][coords[1]]))
		if match {
			next = append(next, [2]int{coords[0] - 1, coords[1]})
		}
	}

	look_below, _ := regexp.MatchString(`[SF7|]`, current_symbol)
	if coords[0] < len(*maze)-1 && look_below {
		match, _ := regexp.MatchString(`[L|J]`, string((*maze)[coords[0]+1][coords[1]]))
		if match {
			next = append(next, [2]int{coords[0] + 1, coords[1]})
		}
	}

	look_left, _ := regexp.MatchString(`[S\-7J]`, current_symbol)
	if coords[1] > 0 && look_left {
		match, _ := regexp.MatchString(`[F\-L]`, string((*maze)[coords[0]][coords[1]-1]))
		if match {
			next = append(next, [2]int{coords[0], coords[1] - 1})
		}
	}

	look_right, _ := regexp.MatchString(`[SF\-L]`, current_symbol)
	if coords[1] < len((*maze)[coords[0]])-1 && look_right {
		match, _ := regexp.MatchString(`[7\-J]`, string((*maze)[coords[0]][coords[1]+1]))
		if match {
			next = append(next, [2]int{coords[0], coords[1] + 1})
		}
	}

	return next
}

func get_next_step(maze *[]string, current [2]int, prev [2]int) [2]int {
	steps := find_adjacent(maze, current)

	if reflect.DeepEqual(steps[0], prev) {
		return steps[1]
	} else {
		return steps[0]
	}
}

func part1(maze *[]string, maze_cells *[][2]int, start_coords *[2]int) {
	*start_coords, _ = find_start(maze)
	*maze_cells = append(*maze_cells, *start_coords)
	steps := 1

	starting_steps := find_adjacent(maze, *start_coords)
	curr := starting_steps[0]
	*maze_cells = append(*maze_cells, curr)
	var prev [2]int = *start_coords
	final_step := starting_steps[1]

	for {
		steps++
		if reflect.DeepEqual(curr, final_step) {
			break
		}
		next := get_next_step(maze, curr, prev)
		*maze_cells = append(*maze_cells, next)
		prev = curr
		curr = next
	}
	fmt.Println("Part 1:", steps/2)
}

func part2(maze *[]string, maze_cells *[][2]int) {
	replace_s(maze)
	total := 0

	for line := range *maze {
		for char := 0; char < len((*maze)[line])-1; char++ {
			ignore := false
			// is this on the line?
			for i := range *maze_cells {
				if (*maze_cells)[i] == [2]int{line, char} {
					ignore = true
					break
				}
			}

			if ignore {
				continue
			}

			num_intersects := 0
			prev_dir := 0
			// |  +1
			// -  no change
			// F  no change, prev_dir = -1
			// 7  if prev_dir = 1, +1; if prev_dir = -1, no change , prev_dir = 0
			// L  no change, prev_dir = 1
			// J  if prev_dir = -1, +1; if prev_dir = -1, no change, prev_dir = 0
			for cell := char; cell < len((*maze)[line])-1; cell++ {
				// check if next char is a mapline cell
				map_line_cell := false
				for i := range *maze_cells {
					if (*maze_cells)[i] == [2]int{line, cell + 1} {
						map_line_cell = true
						break
					}
				}
				if map_line_cell == true {
					switch (*maze)[line][cell+1] {
					case '|':
						num_intersects++
					case 'F':
						prev_dir = -1
					case '7':
						if prev_dir == 1 {
							num_intersects++
						}
						prev_dir = 0
					case 'L':
						prev_dir = 1
					case 'J':
						if prev_dir == -1 {
							num_intersects++
						}
						prev_dir = 0
					}
				}
			}

			if num_intersects%2 != 0 {
				total++
			}
		}
	}
	fmt.Println("Part 2:", total)
}

func replace_s(maze *[]string) {
	start, _ := find_start(maze)
	adj := find_adjacent(maze, start)
	neighbors := [4]int{0, 0, 0, 0}
	//                  L  R  T  B
	for cell := range adj {
		if start[0] == adj[cell][0] {
			// adj is on same line
			if start[1] > adj[cell][1] {
				// same line, before
				neighbors[0] = 1
			} else {
				// same line, after
				neighbors[1] = 1
			}
		} else {
			// adj is in same column
			if start[0] > adj[cell][0] {
				// same col, before
				neighbors[2] = 1
			} else {
				// same col, after
				neighbors[3] = 1
			}
		}
	}

	var start_line string = (*maze)[start[0]]
	switch neighbors {
	case [4]int{1, 0, 1, 0}:
		start_line = strings.Replace(start_line, "S", "J", 1)
	case [4]int{0, 1, 1, 0}:
		start_line = strings.Replace(start_line, "S", "L", 1)
	case [4]int{0, 1, 0, 1}:
		start_line = strings.Replace(start_line, "S", "F", 1)
	case [4]int{1, 0, 0, 1}:
		start_line = strings.Replace(start_line, "S", "7", 1)
	case [4]int{0, 0, 1, 1}:
		start_line = strings.Replace(start_line, "S", "|", 1)
	case [4]int{1, 1, 0, 0}:
		start_line = strings.Replace(start_line, "S", "-", 1)
	}

	(*maze)[start[0]] = strings.Replace(start_line, "S", "J", 1)
}

func main() {
	maze := []string{}
	load_data(&maze)
	maze_cells := [][2]int{}
	start_coords := [2]int{}

	part1(&maze, &maze_cells, &start_coords)
	part2(&maze, &maze_cells)
}

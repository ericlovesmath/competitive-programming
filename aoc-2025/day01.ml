(* Parsing *)

let input =
  open_in "day01.in"
  |> In_channel.input_all
  |> String.trim
  |> String.split_on_char '\n'
  |> List.map (String.map (function 'L' -> '-' | 'R' -> '+' | c -> c))
  |> List.map int_of_string

(* Part 1 *)

let count_scan f =
  let step (cnt, acc) d = (cnt + f acc d, (acc + d) mod 100) in
  fst (List.fold_left step (0, 50) input)

let part1 = count_scan (fun acc _ -> if acc = 0 then 1 else 0)

(* Part 2 *)

(* Yes I could have just used math, no I didn't want to think about it *)
let zeros_in start len =
  let range = 
    if len > 0
      then List.init len (( + ) start)
      else List.init (-len) (( - ) start)
  in
  range
  |> List.filter (fun n -> n mod 100 = 0)
  |> List.length

let part2 = count_scan zeros_in

let () = Printf.printf "Part 1 = %d, Part 2 = %d\n" part1 part2

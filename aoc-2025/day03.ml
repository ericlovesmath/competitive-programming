let input =
  let parse_row s =
    s
    |> String.to_seq
    |> List.of_seq
    |> List.map (fun c -> int_of_char c - int_of_char '0')
  in
  open_in "day03.in"
  |> In_channel.input_all
  |> String.trim
  |> String.split_on_char '\n'
  |> List.map parse_row

let largest_sub target row =
  let rec aux stack deletions = function
    | [] -> List.rev stack
    | hd :: tl ->
        let rec pop s d =
          match s with
          | hd' :: tl' when d > 0 && hd > hd' -> pop tl' (d - 1)
          | _ -> s, d
        in
        let stack, remaining_deletions = pop stack deletions in
        aux (hd :: stack) remaining_deletions tl
  in
  row
  |> aux [] (List.length row - target)
  |> List.take target
  |> List.fold_left (fun acc d -> acc * 10 + d) 0 

let solve n = List.fold_left ( + ) 0 (List.map (largest_sub n) input)
let part1 = solve 2
let part2 = solve 12

let () = Printf.printf "Part 1 = %d, Part 2 = %d\n" part1 part2

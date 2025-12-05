module PointSet = Set.Make (struct
    type t = int * int

    let compare (x, y) (x', y') = if x = x' then compare y y' else compare x x'
  end)

let input =
  open_in "day04.in"
  |> In_channel.input_all
  |> String.trim
  |> String.split_on_char '\n'
  |> List.mapi (fun row line ->
    line
    |> String.to_seq
    |> Seq.mapi (fun col ch -> row, col, ch)
    |> Seq.filter_map (fun (r, c, ch) -> if ch = '@' then Some (r, c) else None)
    |> List.of_seq)
  |> List.concat
  |> PointSet.of_list
;;

let neighbors (x, y) =
  List.map
    (fun (dx, dy) -> x + dx, y + dy)
    [ -1, -1; -1, 0; -1, 1; 0, -1; 0, 1; 1, -1; 1, 0; 1, 1 ]
;;

let is_movable points p =
  let is_paper = Fun.flip PointSet.mem points in
  is_paper p && List.(length (find_all is_paper (neighbors p))) < 4
;;

(* Fix point iteration to remove movable points *)
let rec fix points =
  let movable = PointSet.filter (is_movable points) points in
  if PointSet.is_empty movable then points else fix (PointSet.diff points movable)
;;

let part1 = PointSet.(cardinal (filter (is_movable input) input))
let part2 = PointSet.(cardinal (diff input (fix input)))
let () = Printf.printf "Part 1 = %d, Part 2 = %d\n" part1 part2

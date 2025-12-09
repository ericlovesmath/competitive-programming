{
  description = "Advent of Code 2025";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };
  outputs =
    { nixpkgs, ... }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      devShells.${system}.default =
        pkgs.mkShell {
          packages = [
            pkgs.uiua
            pkgs.pypy3
            (pkgs.python3.withPackages (pkgs: with pkgs; [
              pandas
              numpy
              networkx
              z3-solver
              shapely
            ]))
          ];
        };
    };
}

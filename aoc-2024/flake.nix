{
  description = "Advent of Code 2024";
  inputs = {
    nixpkgs-unstable.url = "github:NixOS/nixpkgs/nixos-unstable";
  };
  outputs =
    { nixpkgs-unstable, ... }:
    let
      system = "aarch64-darwin";
    in
    {
      devShells.${system}.default =
        let
          pkgs = import nixpkgs-unstable { inherit system; };
        in
        pkgs.mkShell {
          packages = [
            pkgs.pypy3
            (pkgs.python3.withPackages (pkgs: with pkgs; [
              pandas
              numpy
            ]))
          ];
        };
    };
}

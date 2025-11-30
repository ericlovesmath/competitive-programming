const std = @import("std");

pub fn build(b: *std.Build) void {
    const target = b.standardTargetOptions(.{});
    const optimize = b.standardOptimizeOption(.{});

    const exe_mod = b.addModule("foo", .{
        .root_source_file = b.path("root.zig"),
        .target = target,
        .optimize = optimize
    });

    // Tester (zls)
    const exe_check = b.addExecutable(.{
        .name = "zig",
        .root_module = exe_mod,
    });

    const check = b.step("check", "Check if zig compiles");
    check.dependOn(&exe_check.step);
}

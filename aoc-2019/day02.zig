const std = @import("std");
const input = @embedFile("day02.in");

const allocator = std.heap.page_allocator;

/// Duplicates [data] and simulates
fn simulate(data: std.ArrayList(usize), noun: usize, verb: usize) !usize {
    var local_data = try data.clone(allocator);
    defer local_data.deinit(allocator);

    var slice = local_data.items;
    slice[1] = noun;
    slice[2] = verb;

    var pc: usize = 0;
    while (true) {
        switch (slice[pc]) {
            1 => {
                const a = slice[slice[pc + 1]];
                const b = slice[slice[pc + 2]];
                slice[slice[pc + 3]] = a + b;
                pc += 4;
            },
            2 => {
                const a = slice[slice[pc + 1]];
                const b = slice[slice[pc + 2]];
                slice[slice[pc + 3]] = a * b;
                pc += 4;
            },
            99 => break,
            else => unreachable,
        }
    }

    return slice[0];
}

pub fn main() !void {
    var data: std.ArrayList(usize) = .empty;
    defer data.deinit(allocator);

    var it = std.mem.tokenizeScalar(u8, input, ',');
    while (it.next()) |num| {
        const trimmed = std.mem.trim(u8, num, "\n ");
        const n = try std.fmt.parseInt(usize, trimmed, 10);
        try data.append(allocator, n);
    }

    const result1 = try simulate(data, 12, 2);
    std.debug.print("Part 1: {d}\n", .{result1});

    for (0..100) |noun| {
        for (0..100) |verb| {
            const result2 = try simulate(data, noun, verb);
            if (result2 == 19690720) {
                std.debug.print("Part 2: {d}\n", .{noun * 100 + verb});
            }
        }
    }
}

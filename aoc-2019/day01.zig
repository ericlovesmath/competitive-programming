const std = @import("std");
const input = @embedFile("day01.in");

fn part1(data: []u32) u32 {
    var sum: u32 = 0;
    for (data) |n| {
        sum += @max(n / 3, 2) - 2;
    }
    return sum;
}

fn part2(data: []u32) u32 {
    var sum: u32 = 0;
    for (data) |n| {
        var next = n;
        while (next > 0) {
            next = @max(next / 3, 2) - 2;
            sum += next;
        }
    }
    return sum;
}

pub fn main() !void {
    const allocator = std.heap.page_allocator;

    var data: std.ArrayList(u32) = .empty;
    defer data.deinit(allocator);

    var it = std.mem.tokenizeScalar(u8, input, '\n');
    while (it.next()) |row| {
        const n = try std.fmt.parseInt(u32, row, 10);
        try data.append(allocator, n);
    }

    std.debug.print("Part 1: {d}\n", .{part1(data.items)});
    std.debug.print("Part 2: {d}\n", .{part2(data.items)});
}

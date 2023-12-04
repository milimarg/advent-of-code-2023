import java.io.IOException
import java.nio.file.Files
import java.nio.file.Paths
data class IntWrapper(var value: Int)

fun isInt(str: String): Boolean {
    return str.toIntOrNull() != null;
}

fun main() {
    val sum = IntWrapper(0);
    Files.lines(Paths.get("./input.txt")).use {stream -> stream.forEach {
        val numbers = it.split(":").toTypedArray()[1].split("|").toTypedArray();
        val mine = numbers[0];
        val lottery = numbers[1];
        val points = IntWrapper(1);
        println(mine);
        println("\n");
        println(lottery);
        println("\n");
        val mineNumbers = mine.split(" ").toTypedArray();
        val lotteryNumbers = lottery.split(" ").toTypedArray();
        for (n in mineNumbers) {
            println("-----");
            println(n);
            println(lotteryNumbers.any{it == n && isInt(n)});
            if (lotteryNumbers.any{it == n && isInt(n)}) {
                points.value *= 2;
            }
        }
        points.value /= 2;
        println("points = ");
        println(points.value);
        println("\n\n");
        sum.value += points.value;
    }};
    println("sum =");
    println(sum.value);
}

import java.io.IOException
import java.nio.file.Files
import java.nio.file.Paths
import java.io.File
data class IntWrapper(var value: Int)

fun isInt(str: String): Boolean {
    return str.toIntOrNull() != null;
}

fun processLine(input: Array<String>, id: Int): Int {
    val numbers = input[id].split(":").toTypedArray()[1].split("|").toTypedArray();
    val mine = numbers[0];
    val lottery = numbers[1];
    val points = IntWrapper(1);
    val copyLen = IntWrapper(0);
    val mineNumbers = mine.split(" ").toTypedArray();
    val lotteryNumbers = lottery.split(" ").toTypedArray();
    for (n in mineNumbers) {
        if (lotteryNumbers.any{it == n && isInt(n)}) {
            copyLen.value++;
        }
    }
    for (j in 1..copyLen.value) {
        points.value += processLine(input, id + j);
    }
    return points.value;
}

fun main() {
    val sum = IntWrapper(0);
    val input = File("./input.txt").readText();
    val inputArray = input.split("\n").toTypedArray();

    for (i in inputArray.indices) {
        sum.value += processLine(inputArray, i);
    }
    println("sum = " + sum.value);
}

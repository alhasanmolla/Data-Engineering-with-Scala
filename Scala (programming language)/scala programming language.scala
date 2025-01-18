// Databricks notebook source
// MAGIC %md
// MAGIC Scala & print Command

// COMMAND ----------

print("go")
print("to home")

// COMMAND ----------

// MAGIC %md
// MAGIC Scala & println Command

// COMMAND ----------

println("go")
println("to home")

// COMMAND ----------

print(10)

// COMMAND ----------

// MAGIC %md
// MAGIC Variables

// COMMAND ----------

val x = 100
println(x)

// COMMAND ----------

// MAGIC %md
// MAGIC Concatenate

// COMMAND ----------

val c = 10
val b = 100

println(c * b)

// COMMAND ----------

val a = "al lhasan"
val f = " fotema"

val love = a + f

println(love)

// COMMAND ----------

val i = 101
val j = 1212

val k = i.toString + j.toString

println(k)

// COMMAND ----------

val i = 101
val j = 1212

val k = i + j

println(k)

// COMMAND ----------

// MAGIC %md
// MAGIC Data Types Part - 1

// COMMAND ----------

val y = "hello"



// COMMAND ----------

val x : integer = 10

// COMMAND ----------

val x : Integer = 10

// COMMAND ----------

val x = 2147483648

// COMMAND ----------

Int MaxValue

// COMMAND ----------

Int MinValue

// COMMAND ----------

Integer.BYTES

// COMMAND ----------

// MAGIC %md
// MAGIC Data types - Part 2

// COMMAND ----------

val x = 2147483648l

// COMMAND ----------

Long.MaxValue

// COMMAND ----------

Long.MinValue

// COMMAND ----------

val x = "100"



// COMMAND ----------

x + 6

// COMMAND ----------

x.toInt + 6

// COMMAND ----------

// MAGIC %md
// MAGIC Interpolations

// COMMAND ----------

val x = 100

// COMMAND ----------

print(x)

// COMMAND ----------

println("This value of variable x is :-" + x)

// COMMAND ----------

println(s"This value of variable x is :- $x")

// COMMAND ----------

val a = - 100.12345

// COMMAND ----------

println(f"this value of variable x is : $a%.2f")

// COMMAND ----------

println("hello \n world")

// COMMAND ----------

println(raw"hello \n world")

// COMMAND ----------

// MAGIC %md
// MAGIC Comparisons

// COMMAND ----------

"a" == "a"

// COMMAND ----------

"a" == "A"

// COMMAND ----------

"a".toLowerCase == "A".toLowerCase

// COMMAND ----------

"a".equalsIgnoreCase("A")

// COMMAND ----------

val x = 10
val y = 10

x == y 

// COMMAND ----------

val x = 10
val y = 10

x != y 

// COMMAND ----------

val x = 10
val y = 20

x != y 

// COMMAND ----------

val x = 10
val y = 20

x > y 

// COMMAND ----------

val x = 20
val y = 20

x >= y 

// COMMAND ----------

val x = 201
val y = 202

x <= y 

// COMMAND ----------

// MAGIC %md
// MAGIC  If else - Part 1

// COMMAND ----------

if (10 > 5)

println("First number is greater than second")

// COMMAND ----------

if (10 > 50)

println("First number is greater than second")

else

println("First number is smaller than second")

// COMMAND ----------

if (10 > 50){
    println("antum")
    println("First number is greater than second")
}

else{
    println("anta")
    println("First number is smaller than second")
}

// COMMAND ----------

// MAGIC %md
// MAGIC If else - Part 2

// COMMAND ----------

if (20 > 100) "yes" else "no"

// COMMAND ----------

if (10 > 20) println("yes") else println("no")

// COMMAND ----------

val result = if (20 > 100) "yes" else "no"

// COMMAND ----------

if (6 > 5 && 6 < 10)
  println("yes")

else
  println("no")

// COMMAND ----------

if (6 > 5 && 6 < 10 && 5 < 100)
  println("yes")

else
  println("no")

// COMMAND ----------

if (6 > 5 && 6 < 10 && 500 < 100)
  println("yes")

else
  println("no")

// COMMAND ----------

if (6 > 5 6 < 10)

// COMMAND ----------

// MAGIC %md
// MAGIC  If else if

// COMMAND ----------

val x  = 89

if (x >= 90){

  println("Excellent")
}

else {

  println("low")
}

// COMMAND ----------

val x  = 71

if (x >= 90){

  println("Excellent")
}

else if (x >= 80){

  println("Good")
}

else if (x >= 70){

  println("avarage")
}

else {

  println("low")
}

// COMMAND ----------

// MAGIC %md
// MAGIC Match Case

// COMMAND ----------

val monthnum = 12

monthnum match{

  case 1 => println("Jan")
  case 2 => println("Feb")
  case 3 => println("Mar")
  case 4 => println("Apr")
  case 5 => println("May")
  case 6 => println("Jun")
  case 7 => println("Jul")
  case 8 => println("Aug")
  case 9 => println("Sep")
  case 10 => println("Oct")
  case 11 => println("Nove")
  case 12 => println("Dec")
  case _ => println("Invalid month number")

}

// COMMAND ----------

val item = "Bananas"

item match{

  case "Oranges" => println("1 kg = 10$ ")
  case "Apple" => println("1 kg = 12$ ")
  case "Bananas" => println("1 kg = 8$ ")
  case _ => println("others")


}

// COMMAND ----------

val x = 91

x match{

  case a if (x >= 90) => println("Excelent")
  case a if (x >= 80) => println("Good")
  case a if (x >= 65) => println("Average")
  case _ => println("Low")

}

// COMMAND ----------

val item = "Tomatoes"

item match {
  case "Oranges" | "Apples" | "Bananas" => println("fruits category")
  case "Onion" | "Tomatoes" | "Potatoes" => println("vegetables category")
  case _ => println("others")
}

// COMMAND ----------

// MAGIC %md
// MAGIC For Loop

// COMMAND ----------

for (i <- 1 to 10) println(i)

// COMMAND ----------

for (i <- 1 to 10){
  println(i)
  println(i * 10)
}

// COMMAND ----------

for (i <- 1 to 10 by 2){
  println(i)
  println(i * 99)
}

// COMMAND ----------

for (i <- 10 to 1 by -1){
  println(i)
  println(i * 99)
}

// COMMAND ----------

(1 to 10).foreach(println)

// COMMAND ----------

// MAGIC %md
// MAGIC While Loop

// COMMAND ----------

var i = 10

// COMMAND ----------

i += 1

// COMMAND ----------

i

// COMMAND ----------

var j = 0

// COMMAND ----------

var j = 0

while (j < 5){
  println(j)
  j += 1
}

// COMMAND ----------

// MAGIC %md
// MAGIC Do While Loop

// COMMAND ----------

var x = 5


while (x < 5){

  println(s"This value of x is $x")
}

// COMMAND ----------

var y = 5 

do {
  println(s"This value of x is $x")
  y += 1
}while(x < 5)

// COMMAND ----------

// MAGIC %md
// MAGIC Break In Loop

// COMMAND ----------

for (i <- 1 to 10){
  if (i < 5){
    println(i)
  }
}


// COMMAND ----------

for (i <- 1 to 10){
  if (i < 5){
    println(i)
  }else{
    println("no")
  }
}

// COMMAND ----------

import scala.util.control.Breaks._

breakable{
  for (i <- 1 to 10){
  if (i < 5){
    println(i)
  }else{
    break
  }
}
}

// COMMAND ----------

import scala.util.control.Breaks._

breakable{
  for (i <- 1 to 10){
  if (i < 5){
    println(i)
  }else{
    break
  }
}
}

val x = 100

// COMMAND ----------



breakable{
  for (i <- 1 to 10){
  if (i < 5){
    break
  }else{
    println(i)
  }
}
}

val x = 100 

// COMMAND ----------

  for (i <- 1 to 10){  
  breakable{
  if (i < 5){
    break
  }else{
    println(i)
  }
}
}

val x = 100 

// COMMAND ----------

// MAGIC %md
// MAGIC List Collection

// COMMAND ----------

val names= List("Joel", "Chris", "Ed")

// COMMAND ----------

val names: List[String] = List("Joel", "Chris", "Ed")


// COMMAND ----------

val existingList = List(1, 2, 3)
val appendedList = existingList :+ 4 // Append 4 to the existing list



// COMMAND ----------

val prependedList = 0 +: existingList // Prepend 0 to the existing list


// COMMAND ----------

val myList = List(-1, 0)
val newList = myList ++ List(1, 2, 3) // Combine myList with additional elements


// COMMAND ----------

val names = List("Joel", "Chris", "Ed")
for (name <- names) {
  println(name)
}


// COMMAND ----------

val lst = 1::2::8::8::Nil


// COMMAND ----------

val last2 = "India"::"Uk"::"US"::Nil

// COMMAND ----------

for (name <- last2) {
  println(name)
}

// COMMAND ----------

val emptylist = Nil

// COMMAND ----------

val rngtolist = (1 to 10).toList

// COMMAND ----------

val rnglist2 = List.range(1,10)

// COMMAND ----------

val charlist = List.range('a','z')

// COMMAND ----------

val lst = (1 to 10).toList

// COMMAND ----------

lst(2)

// COMMAND ----------

val last2 = "India"::"Uk"::"US"::Nil

// COMMAND ----------

last2(2)

// COMMAND ----------

last2(0)

// COMMAND ----------

last2(0) ="Ind"

// COMMAND ----------

val mixlist = List(10,"a",20,"b")

// COMMAND ----------

// MAGIC %md
// MAGIC List Collection - Part 2

// COMMAND ----------

val lst = List.range(1,11)

// COMMAND ----------

lst.length

// COMMAND ----------

val CnList = List("India","UK","US","Germany")

// COMMAND ----------

CnList.length

// COMMAND ----------

lst(0)

// COMMAND ----------

lst.head

// COMMAND ----------

lst.slice(0,3)

// COMMAND ----------

lst.slice(4,6)

// COMMAND ----------

 lst.init

// COMMAND ----------

lst.tail

// COMMAND ----------

lst.reverse

// COMMAND ----------

val newlist = lst.reverse.slice(0,3).reverse

// COMMAND ----------

// MAGIC %md
// MAGIC List Collection - Part 3

// COMMAND ----------

CnList

// COMMAND ----------

CnList.foreach(println)

// COMMAND ----------

for (i <- CnList){
  println(i)
}

// COMMAND ----------

CnList.contains("UK")

// COMMAND ----------

if (CnList.contains("UK")){
  println("Item found in list")
}else{
  println("Item not found in list")
}

// COMMAND ----------

if (CnList.contains("Bangladesh")){
  println("Item found in list")
}else{
  println("Item not found in list")
}

// COMMAND ----------

CnList.startsWith(Seq("India"))

// COMMAND ----------

CnList.endsWith(Seq("US","Germany"))

// COMMAND ----------

val lst = List(5,2,7,1)

// COMMAND ----------

lst.sorted

// COMMAND ----------

lst.sorted(Ordering.Int.reverse)

// COMMAND ----------

CnList.sorted

// COMMAND ----------

CnList.sorted(Ordering.String.reverse)

// COMMAND ----------

lst.mkString

// COMMAND ----------

CnList.mkString

// COMMAND ----------

CnList.mkString("-")

// COMMAND ----------

lst.sum

// COMMAND ----------

lst.max

// COMMAND ----------

lst.min

// COMMAND ----------

val lst2 = List.range(1,11)

// COMMAND ----------

lst2.take(5)

// COMMAND ----------

lst2.drop(5)

// COMMAND ----------

lst2.drop(5).take(3)

// COMMAND ----------

// MAGIC %md
// MAGIC List Collection - Part 4

// COMMAND ----------

val lst = List.range(1,11)

// COMMAND ----------

lst.indices

// COMMAND ----------

val lst2 = List.range(5,8)

// COMMAND ----------

val lst3 = lst.union(lst2)

// COMMAND ----------

lst.distinct

// COMMAND ----------

lst3.distinct

// COMMAND ----------

val lst3 = lst.union(lst2).distinct

// COMMAND ----------

lst.diff(lst2)

// COMMAND ----------

lst.intersect(lst2)

// COMMAND ----------

lst.sliding(2)

// COMMAND ----------

lst.sliding(2)

// COMMAND ----------

val newlist = lst.sliding(2).toList

// COMMAND ----------

val newlist = lst.sliding(2,2).toList

// COMMAND ----------

val newlist2 = lst.sliding(3,2).toList

// COMMAND ----------

newlist.flatten

// COMMAND ----------

List.fill(3)(10)

// COMMAND ----------

List.fill(4)("hello")

// COMMAND ----------

// MAGIC %md
// MAGIC List Collection Part 5

// COMMAND ----------

val lst = List.range(1,11)

// COMMAND ----------

lst.filter(x => x == 2)

// COMMAND ----------

lst.filter(i => i > 2)

// COMMAND ----------

val newlist = lst.filter(k => k != 3)

// COMMAND ----------

lst.filter(x => x%2 == 0)

// COMMAND ----------

lst.filter(x => x%2 == 1)

// COMMAND ----------

val dblist = lst.map(x => x+2)

// COMMAND ----------

val dblist = lst.map(x => x*2)

// COMMAND ----------

dblist

// COMMAND ----------

val strlist = List("india","uk","usa")

// COMMAND ----------

strlist.map(x => x.toUpperCase)

// COMMAND ----------

lst.partition(x => x%2 ==0)

// COMMAND ----------

// MAGIC %md
// MAGIC List Buffer

// COMMAND ----------

import scala.collection.mutable.ListBuffer

val lstb = ListBuffer[Int]()

// COMMAND ----------

lstb += 1

// COMMAND ----------

lstb += 2 

// COMMAND ----------

lstb(0) = 100

// COMMAND ----------

lstb

// COMMAND ----------

lstb -= 2 

// COMMAND ----------

lstb -= 1 

// COMMAND ----------

lstb += 3

lstb += 4

// COMMAND ----------

lstb

// COMMAND ----------

val lst = lstb.toList

// COMMAND ----------

val lstb2 = ListBuffer[Int]()

// COMMAND ----------

for (i <- 1 to 10){
  lstb2 += i
}

// COMMAND ----------

lstb2

// COMMAND ----------

// MAGIC %md
// MAGIC Anonymous Function

// COMMAND ----------

val lst = List.range(1,11)

// COMMAND ----------

lst.filter(x => x > 5)

// COMMAND ----------

lst.filter((x:Int) => x > 5)

// COMMAND ----------

lst.filter(_ > 5)

// COMMAND ----------

lst.map(x => x * 2)

// COMMAND ----------

lst.map(_ * 2)

// COMMAND ----------

val strlist = List("India","UK","USA")

// COMMAND ----------

strlist.map(x => x.toLowerCase)

// COMMAND ----------

val tolowercase = strlist.map(_ toLowerCase)

// COMMAND ----------

tolowercase

// COMMAND ----------

// MAGIC %md
// MAGIC Array collection - Part 1

// COMMAND ----------

val arr = Array(1,2,3,4)

// COMMAND ----------

arr(0)

// COMMAND ----------

val arr2 = Array("India","UK","US")

// COMMAND ----------

arr2(0)

// COMMAND ----------

val arr3 = (1 to 10).toArray

// COMMAND ----------

val arr4 = Array.range(1,11)

// COMMAND ----------

arr4(0) = 100

// COMMAND ----------

arr4

// COMMAND ----------

import scala.collection.mutable.ArrayBuffer

val arrb = ArrayBuffer[Int]()

// COMMAND ----------

arrb += 1
arrb += 2
arrb += 3

// COMMAND ----------

arrb

// COMMAND ----------

arrb -=2

// COMMAND ----------

val arr2b = ArrayBuffer[Int](10,20,30)

// COMMAND ----------

import scala.collection.mutable.ListBuffer


val lstb = ListBuffer[String]("India","UK","US")

// COMMAND ----------

lstb += "Germany"

// COMMAND ----------

lstb -= "UK"

// COMMAND ----------

// MAGIC %md
// MAGIC Array collection Part 2

// COMMAND ----------

val arrmultidin = Array.ofDim[Int](2,2)

// COMMAND ----------

arrmultidin(0)(0) = 10
arrmultidin(0)(1) = 20
arrmultidin(1)(0) = 30
arrmultidin(1)(1) = 40

// COMMAND ----------

arrmultidin

// COMMAND ----------

arrmultidin(2)(0)

// COMMAND ----------

arrmultidin(1)(0)

// COMMAND ----------

val arrmultidin = Array.ofDim[Int](5,2)

// COMMAND ----------

val arrmultidin = Array.ofDim[Int](5,3)

// COMMAND ----------

// MAGIC %md
// MAGIC Set Collection

// COMMAND ----------

val st = Set(1,2,3,4)

// COMMAND ----------

val st2 = Set ("india","uk","us")

// COMMAND ----------

val st3 = Set(1,2,1,1,2,2,3)

// COMMAND ----------

val stm = collection.mutable.Set(1,2,3,4)

// COMMAND ----------

stm += 5

// COMMAND ----------

// MAGIC %md
// MAGIC Tuple

// COMMAND ----------

val tup = (1,"India",10000,"Laptop")

// COMMAND ----------

tup.getClass

// COMMAND ----------

tup._4

// COMMAND ----------

// MAGIC %md
// MAGIC Map Collection

// COMMAND ----------

val mp = Map(1 -> "India", 2 -> "US", 3 -> "UK")

// COMMAND ----------

mp(1)

// COMMAND ----------

mp(3)

// COMMAND ----------

mp(1) = "india"

// COMMAND ----------

val mpm = collection.mutable.Map(1 -> "India", 2 -> "US", 3 -> "UK")

// COMMAND ----------

mpm(1) = "india"

// COMMAND ----------

mpm

// COMMAND ----------

val mpm = collection.mutable.Map("key1" -> "India", "key2" -> "US", "key3" -> "UK")

// COMMAND ----------

mpm("key3")

// COMMAND ----------

for ( i <- mp){
  println(i)
}

// COMMAND ----------

val mp2 = Map("key1" -> "India", "key2" -> "US", "key3" -> "UK")

// COMMAND ----------

mp2("key2")

// COMMAND ----------

val tup = "key1" -> "India"

// COMMAND ----------

tup.getClass

// COMMAND ----------

for ( i <- mp.keys){
  println(i)
}

// COMMAND ----------

for ( i <- mp.values){
  println(i)
}

// COMMAND ----------

for ( (k,v) <- mp){
  println(s"This key is $k and value is $v")
}

// COMMAND ----------

val mp = Map(1 -> 100, 2 -> 200, 1 -> 300)

// COMMAND ----------

// MAGIC %md
// MAGIC String operations – Part 1

// COMMAND ----------

val x = "hellow"

// COMMAND ----------

x(1)

// COMMAND ----------

x(0)

// COMMAND ----------

x(7)

// COMMAND ----------

x.length

// COMMAND ----------

x(x.length-1)

// COMMAND ----------

x(x.length-2)

// COMMAND ----------

x.indices

// COMMAND ----------

x.head

// COMMAND ----------

x.tail

// COMMAND ----------

x.last

// COMMAND ----------

x.take(1)

// COMMAND ----------

x.take(3)

// COMMAND ----------

x.slice(0,3)

// COMMAND ----------

x.substring(0,4)

// COMMAND ----------

x.drop(3)

// COMMAND ----------

x.dropRight(1)

// COMMAND ----------

x.filterNot(_ == 'e')

// COMMAND ----------

x.replaceFirst("ell", "")

// COMMAND ----------

x.toUpperCase

// COMMAND ----------

x.toLowerCase

// COMMAND ----------

val y = "hello world"

// COMMAND ----------

y.capitalize

// COMMAND ----------

val a = "hello"
val b = "Hello"

// COMMAND ----------

a == b

// COMMAND ----------

val a = "hello"
val b = "hello"

// COMMAND ----------

a == b

// COMMAND ----------

a.equals(b)

// COMMAND ----------

a.equalsIgnoreCase(b)

// COMMAND ----------

// MAGIC %md
// MAGIC String operations – Part 2

// COMMAND ----------

x.contains("ea")

// COMMAND ----------

x.contains("e")

// COMMAND ----------

if (x.contains("e")) {
  println("String contains")
} else {
  println("String doesn't contain")
}

// COMMAND ----------

x.exists("e")

// COMMAND ----------

x.exists(a => a == 'e')

// COMMAND ----------

x.startsWith("he")

// COMMAND ----------

x.endsWith("o")

// COMMAND ----------

for (i <- x){
  println(i)
}

// COMMAND ----------

val y ="   hello  "

// COMMAND ----------

y.trim

// COMMAND ----------

y.trim.toList

// COMMAND ----------

val a = "hello"
val b = " world"

// COMMAND ----------

a + b

// COMMAND ----------

a.concat(b)

// COMMAND ----------

x.distinct

// COMMAND ----------

x.filter(a=>a=='e')

// COMMAND ----------

x.filter(_ == 'e')

// COMMAND ----------

x.filter(a=>a!='e')

// COMMAND ----------

x.filterNot(a=>a=='e')

// COMMAND ----------

x.replace('e','x')

// COMMAND ----------

x.replace('l','x')

// COMMAND ----------

x.replaceFirst("l","x")

// COMMAND ----------

x.replaceFirst("ll","x")

// COMMAND ----------

// MAGIC %md
// MAGIC yield

// COMMAND ----------

val lst = List(1,2,3,4,5)

// COMMAND ----------

for (i <- lst){
  println(i )
}

// COMMAND ----------

for (i <- lst) yield i 

// COMMAND ----------

for (i <- lst) yield i * 2

// COMMAND ----------

lst.map(_ * 2)

// COMMAND ----------

for (i <- lst) yield {i * 2}

// COMMAND ----------

val lst2 = List("india","uk","us")

// COMMAND ----------

lst2.map(_ .toUpperCase)

// COMMAND ----------

lst2.map(x=>x.toUpperCase)

// COMMAND ----------

for (i <- lst2) yield i.toUpperCase

// COMMAND ----------

for (i <- lst2) yield i.take(1).toUpperCase

// COMMAND ----------

for (i <- lst2) yield{
  val initial = i.take(1)
  val convertupper = initial.toUpperCase
  convertupper
}

// COMMAND ----------

lst2.map(x=>x.take(1).toUpperCase)

// COMMAND ----------

// MAGIC %md
// MAGIC Scala type hierarchy

// COMMAND ----------



// COMMAND ----------

// MAGIC %md
// MAGIC  Nil

// COMMAND ----------

val lst = List ()

// COMMAND ----------

val lst = List(1,2,3,4)

// COMMAND ----------

val lst2 = List("a","b","d")

// COMMAND ----------

val lst3 = List(1,"a",2,3)

// COMMAND ----------

val lst4 = Nil

// COMMAND ----------

val lst5 = 1::2::3::Nil

// COMMAND ----------

// MAGIC %md
// MAGIC Null

// COMMAND ----------

val x = null

// COMMAND ----------

val y = "hello"

// COMMAND ----------

var a : Int = 100

// COMMAND ----------

a = null

// COMMAND ----------

val i :Double = null

// COMMAND ----------

val b :String = null

// COMMAND ----------

b(0)

// COMMAND ----------

val k = "hello"

// COMMAND ----------


    val name: Option[String] = None // Using Option to represent absence of a value

    // Safely handle the value
    name match {
      case Some(value) => println(s"Name is: $value")
      case None => println("Name is not provided")
    }

    // Example with a value
    val anotherName: Option[String] = Some("Alice")

    anotherName match {
      case Some(value) => println(s"Name is: $value")
      case None => println("Name is not provided")
    }

// COMMAND ----------


    val name: String = null // A variable explicitly set to null

    // Check for null before using the variable
    if (name == null) {
      println("Name is null")
    } else {
      println(s"Name is: $name")
    }

// COMMAND ----------

    val name: String = "hasan" // A variable explicitly set to null

    // Check for null before using the variable
    if (name == null) {
      println("Name is null")
    } else {
      println(s"Name is: $name")
    }

// COMMAND ----------

// MAGIC %md
// MAGIC Try Catch

// COMMAND ----------

val x = 100/0

// COMMAND ----------

val y = "a".toInt

// COMMAND ----------

try{
  
  val x = 100/2

}catch{
  case e: ArithmeticException =>println("Cannot divide by zero")
}

// COMMAND ----------

val divisor = 0

if (divisor != 0) {
  val x = 100 / divisor
  println(s"This is ans: $x")
} else {
  println("Cannot divide by zero")
}

// COMMAND ----------

try{
  
  val x = "a".toInt

}catch{
  case e: ArithmeticException =>println("Cannot divide by zero")
}

// COMMAND ----------

try{
  
  val x = "a".toInt

}catch{
  case e: NumberFormatException =>println("Cannot convert string to integer")
}

// COMMAND ----------

try{
  val lst = List(1,2,3,4)
  lst(2)
}catch{
  case e: IndexOutOfBoundsException =>{println("cannot access 5th index")}
}finally{
  println("This will run everytime")
}

// COMMAND ----------

// MAGIC %md
// MAGIC Try Success Failure

// COMMAND ----------

import scala.util.{Try,Success,Failure}

// COMMAND ----------

Try{
  180
}

// COMMAND ----------

Try{
  100/0
}

// COMMAND ----------

Try{
  "a".toInt
}

// COMMAND ----------

Try{
  "1".toInt
}

// COMMAND ----------

val result = Try{
  "a".toInt
}


result match{
  case Success(x) => true
  case Failure(y) => false
}

// COMMAND ----------

val result = Try{
  "100".toInt
}


result match{
  case Success(x) => println(x)
  case Failure(y) => println(y)
}

// COMMAND ----------

val result = Try{
  val a = "a".toInt
  a
}


result match{
  case Success(x) => println(x)
  case Failure(y) => println(y)
}

// COMMAND ----------

// MAGIC %md
// MAGIC Datetime – Part 1

// COMMAND ----------

import java.util.Calendar

// COMMAND ----------

val now = Calendar.getInstance.getTime

// COMMAND ----------

val cl = Calendar.getInstance

// COMMAND ----------

cl.get(Calendar.YEAR)

// COMMAND ----------

cl.get(Calendar.MONTH) +1

// COMMAND ----------

cl.get(Calendar.DATE)

// COMMAND ----------

cl.get(Calendar.HOUR)

// COMMAND ----------

cl.get(Calendar.MINUTE)

// COMMAND ----------

cl.get(Calendar.SECOND)

// COMMAND ----------

cl.get(Calendar.MILLISECOND)

// COMMAND ----------

cl.set(Calendar.YEAR,2010)

// COMMAND ----------

cl.getTime

// COMMAND ----------

cl.set(Calendar.MONTH,7)

// COMMAND ----------

cl.getTime

// COMMAND ----------

cl.add(Calendar.YEAR,5)

// COMMAND ----------

cl.getTime

// COMMAND ----------

cl.add(Calendar.YEAR,-2)

// COMMAND ----------

cl.getTime

// COMMAND ----------

cl.add(Calendar.MONTH,5)

// COMMAND ----------

cl.getTime


// COMMAND ----------

cl.add(Calendar.DATE,15)

// COMMAND ----------

cl.getTime

// COMMAND ----------

cl.add(Calendar.HOUR,5)

// COMMAND ----------

cl.getTime

// COMMAND ----------

// MAGIC %md
// MAGIC Datetime – Part 2

// COMMAND ----------

import java.util.Calendar
import java.text.SimpleDateFormat

// COMMAND ----------

val now = Calendar.getInstance.getTime

// COMMAND ----------

val dtfml = new SimpleDateFormat("dd/MM/yyyy")

// COMMAND ----------

dtfml.format(now)

// COMMAND ----------

val dtfm2 = new SimpleDateFormat("dd/MMM/yyyy")

// COMMAND ----------

dtfm2.format(now)

// COMMAND ----------

val dtfm2 = new SimpleDateFormat("dd/MMM/yy")

// COMMAND ----------

dtfm2.format(now)

// COMMAND ----------

val dtfm2 = new SimpleDateFormat("yyyy-MMM-dd")

// COMMAND ----------

dtfm2.format(now)

// COMMAND ----------

val dtfm3 = new SimpleDateFormat("dd-MM-yyyy HH:mm:ss")

// COMMAND ----------

dtfm3.format(now)

// COMMAND ----------

// MAGIC %md
// MAGIC Datetime – Part 3

// COMMAND ----------

import java.time.LocalDateTime
import java.time.LocalDate
import java.time.LocalTime

// COMMAND ----------

LocalDate.now

// COMMAND ----------

import java.time.LocalDate
import java.time.temporal.ChronoUnit

val startDt = LocalDate.of(2010, 1, 15)
val endDt = LocalDate.of(2021, 10, 3)

println("startDt: " + startDt)
println("endDt: " + endDt)

val daysBetween = ChronoUnit.DAYS.between(startDt, endDt)
println("Days between startDt and endDt: " + daysBetween)

// COMMAND ----------

import java.time.LocalDate
import java.time.temporal.ChronoUnit

val startDt = LocalDate.of(2010, 1, 15)
val endDt = LocalDate.of(2021, 10, 3)

println("startDt: " + startDt)
println("endDt: " + endDt)

val daysBetween = ChronoUnit.YEARS.between(startDt, endDt)
println("Years between startDt and endY: " + daysBetween)

// COMMAND ----------

// MAGIC %md
// MAGIC Option

// COMMAND ----------

val mp = Map(1-> "India",2-> "USA")

// COMMAND ----------

mp(1)

// COMMAND ----------

mp(3)

// COMMAND ----------

mp.get(1)

// COMMAND ----------

mp.get(3)

// COMMAND ----------

mp.getOrElse(1,"key not found")

// COMMAND ----------

mp.getOrElse(3,"key not found")

// COMMAND ----------

mp.getOrElse(3,0)

// COMMAND ----------

val x:String = "hello"

// COMMAND ----------

val x:String = null

// COMMAND ----------

val x:Option[String] = Some("hello")

// COMMAND ----------

val x:Option[String] = None

// COMMAND ----------

val country = mp.get(1)


country match{
  case Some(value) => println("key found")
  case None => println("key not found")
}

// COMMAND ----------

// MAGIC %md
// MAGIC Char

// COMMAND ----------

val x = "A"

// COMMAND ----------

val x2 = "AB"

// COMMAND ----------

val y = 'A'

// COMMAND ----------

val y2 = 'AB'

// COMMAND ----------

val y3: Char = 'A'

// COMMAND ----------

val y4: Char = 'AB'

// COMMAND ----------

val myChar: Char = 'A' // Declare a Char with the value 'A'

// Check if the Char is a digit
val isDigit: Boolean = myChar.isDigit

// Convert the Char to its Unicode code point
val unicodeCodePoint: Int = myChar.toInt

println(s"Character: $myChar")
println(s"Is digit? $isDigit")
println(s"Unicode code point: $unicodeCodePoint")


// COMMAND ----------

// MAGIC %md
// MAGIC Regex

// COMMAND ----------

// MAGIC %md
// MAGIC Checking if a Password Contains a Number

// COMMAND ----------

import scala.util.matching.Regex

val numberPattern: Regex = "[0-9]".r

numberPattern.findFirstMatchIn("awesomepassword") match {
  case Some(_) => println("Password OK")
  case None    => println("Password must contain a number")
}


// COMMAND ----------

def saveContactInformation(contact: String): Unit = {
  import scala.util.matching.Regex

  val emailPattern: Regex = """^(\w+)@(\w+(\.\w+)+)$""".r
  val phonePattern: Regex = """^(\d{3}-\d{3}-\d{4})$""".r

  contact match {
    case emailPattern(localPart, domainName, _) =>
      println(s"Hi $localPart, we have saved your email address.")
    case phonePattern(phoneNumber) =>
      println(s"Hi, we have saved your phone number $phoneNumber.")
    case _ =>
      println("Invalid contact information, neither an email address nor phone number.")
  }
}

saveContactInformation("123-454-7890")


// COMMAND ----------

import scala.util.matching.Regex


// COMMAND ----------

val x = "helaloa"

// COMMAND ----------

val pattern = new Regex("a")

// COMMAND ----------

pattern.findFirstIn(x)

// COMMAND ----------

val pattern2 = new Regex("b")
pattern2.findFirstIn(x)

// COMMAND ----------

val x = "helalao"
val pattern = new Regex("l")
val result = pattern.findFirstIn(x)


result match{
  case Some(i) => println("match found")
  case None => println("match not found")
}

// COMMAND ----------

val x = "helalao"
val pattern = new Regex("l")
val result = pattern.findAllIn(x)

result.foreach(println)

// COMMAND ----------

val x = "helalao"
val pattern = new Regex("l")
val result = pattern.findFirstMatchIn(x)

println(result.map(_.start))

// COMMAND ----------

val x = "helalao"
val pattern = new Regex("l")
val result = pattern.findFirstMatchIn(x)

result.map(_.start).foreach(println)

// COMMAND ----------

val x = "helalao"
val pattern = "a".r
val result = pattern.findFirstMatchIn(x)

result.foreach(println)

// COMMAND ----------

import scala.util.matching.Regex

val mystring = "h7dgT98*hT6$R3"
val pattern = new Regex("\\*") // Corrected variable name: 'pettern' -> 'pattern'
val result = pattern.findAllIn(mystring)

result.foreach(println)

// COMMAND ----------

import scala.util.matching.Regex

val mystring = "h7dgT98*hT6$R3"
val pattern = new Regex("\\*") // Corrected variable name: 'pettern' -> 'pattern'
val result = pattern.findFirstMatchIn(mystring)

result.map(_.start).foreach(println)

// COMMAND ----------

import scala.util.matching.Regex

val mystring = "hello world"
val pattern = new Regex("rl\\d") // Corrected variable name: 'pettern' -> 'pattern'
val result = pattern.findAllIn(mystring)

result.foreach(println)

// COMMAND ----------

import scala.util.matching.Regex

val mystring = "hello world"
val pattern = new Regex("rl\\t") // Corrected variable name: 'pettern' -> 'pattern'
val result = pattern.findAllIn(mystring)

result.foreach(println)

// COMMAND ----------

import scala.util.matching.Regex

val mystring = "h7dgT98*hT6$R3"
val pattern = new Regex("\\p{Lower}") // Corrected variable name: 'pettern' -> 'pattern'
val result = pattern.findAllIn(mystring)

result.foreach(println)


// COMMAND ----------

import scala.util.matching.Regex

val mystring = "h7dgT98*hT6$R3"
val pattern = new Regex("\\p{Upper}") // Corrected variable name: 'pettern' -> 'pattern'
val result = pattern.findAllIn(mystring)

result.foreach(println)

// COMMAND ----------

import scala.util.matching.Regex

val mystring = "h7dgT98*hT6$R3"
val pattern = new Regex("\\p{Alpha}") // Corrected variable name: 'pettern' -> 'pattern'
val result = pattern.findAllIn(mystring)

result.foreach(println)

// COMMAND ----------

import scala.util.matching.Regex

val mystring = "h7dgT98*hT6$R3"
val pattern = new Regex("\\p{Digit}") // Corrected variable name: 'pettern' -> 'pattern'
val result = pattern.findAllIn(mystring)

result.foreach(println)

// COMMAND ----------

import scala.util.matching.Regex

val mystring = "h7dgT98*hT6$R3"
val pattern = new Regex("\\p{Alnum}") // Corrected variable name: 'pettern' -> 'pattern'
val result = pattern.findAllIn(mystring)

result.foreach(println)

// COMMAND ----------

import scala.util.matching.Regex

val mystring = "h7dgT98*hT6$R3"
val pattern = new Regex("\\p{Punct}") // Corrected variable name: 'pettern' -> 'pattern'
val result = pattern.findAllIn(mystring)

result.foreach(println)

// COMMAND ----------



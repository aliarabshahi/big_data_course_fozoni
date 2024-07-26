### What is Java?

Java is a popular programming language, created in 1995. It is owned by Oracle, and more than **3 billion** devices run Java. It is used for:

- Mobile applications (specially Android apps)
- Desktop applications
- Web applications
- Web servers and application servers
- Games
- Database connection
- And much, much more!

### Why use Java?

- Java works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc.)
- It is one of the most popular programming languages in the world
- It has a large demand in the current job market
- It is easy to learn and simple to use
- It is open-source and free
- It is secure, fast and powerful
- It has huge community support (tens of millions of developers)
- Java is an object oriented language which gives a clear structure to programs and allows code to be reused, lowering development costs
- As Java is close to C++ and C#, it makes it easy for programmers to switch to Java or vice versa

### Install some tools

1- [Java JDK 8](https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html)

Note: After installation, set the path of bin directory in the path of your system. Note that if you have more than one Java version, **the one that is higher on the list**, works!

2- [Maven](https://maven.apache.org/download.cgi) 

🛑 Just Download [THIS FILE](https://dlcdn.apache.org/maven/maven-3/3.9.6/binaries/apache-maven-3.9.6-bin.zip) and extract it somewhere in your computer like this

```
C:\maven\apache-maven-3.9.6
```

3- [IntelliJ IDEA Community Edition](https://www.jetbrains.com/idea/download/?section=windows) 

### javac and java

When we run a .java file, for example `Test.java` first we should run.

```bash
$ PATH_OF_FILE> javac Test.java
```

Then a file `Test.class` will be created. Java compiler takes `Test.java` and turns it into bytecode. This bytecode is what the **Java Virtual Machine (JVM)** understands and can execute.

Now you can just run this

```bash
$ PATH_OF_FILE> java Test
```

### Build your first Package

Packages are divided into two categories:

- Built-in Packages (packages from the Java API)
- User-defined Packages (create your own packages)

We import packages like this:

```bash
import package.name.Class;   // Import a single class
import package.name.*;   // Import the whole package

import java.util.Scanner;
```

To create a package, use the `package` keyword. Create file `MyPackageClass.java` and paste the following block in it:

```
package mypack;
class MyPackageClass {
  public static void main(String[] args) {
    System.out.println("This is my package!");
  }
}
```

```bash
$ PATH_OF_FILE> javac MyPackageClass.java

$ PATH_OF_FILE> javac -d . MyPackageClass.java
# The -d keyword specifies the destination for where to save the class file. You can use any directory name, like c:/user (windows), or, if you want to keep the package within the same directory, you can use the dot sign ".", like in the example above.

$ PATH_OF_FILE> java mypack.MyPackageClass
```

### Make a simple Maven project

```bash
mkdir -p src/main/java/hello
```

Create a file with name `HelloWorld.java` in `src/main/java/hello/` folder and paste the following lines in it: 

```
package hello;

public class HelloWorld {
  public static void main(String[] args) {
    Greeter greeter = new Greeter();
    System.out.println(greeter.sayHello());
  }
}
```

Also, create a file with name `Greeter.java` in `src/main/java/hello/` folder and paste the following lines in it:

```
package hello;

public class Greeter {
  public String sayHello() {
    return "Hello world!";
  }
}
```

In the root directory of this project create a file `pom.xml` (***POM == Project Object Model***) and paste the following block in it:

```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>ir.m_fozouni</groupId>
    <artifactId>session_13_java</artifactId>
    <packaging>jar</packaging>
    <version>0.1.0</version>

    <properties>
        <maven.compiler.source>1.8</maven.compiler.source>
        <maven.compiler.target>1.8</maven.compiler.target>
    </properties>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-shade-plugin</artifactId>
                <version>3.2.4</version>
                <executions>
                    <execution>
                        <phase>package</phase>
                        <goals>
                            <goal>shade</goal>
                        </goals>
                        <configuration>
                            <transformers>
                                <transformer
                                    implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                                    <mainClass>hello.HelloWorld</mainClass>
                                </transformer>
                            </transformers>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

### Now Build the project

```bash
$ mvn install

$ mvn compiler:compile
```

Now go to the root directory. You should see the `target` directory. Explore it carefully.    

🛑 **Note:** For the first time that we run `mvn compile` we would get an error. So go to this link and follow the instructions

https://cwiki.apache.org/confluence/display/MAVEN/LifecyclePhaseNotFoundException

### Run the jar file by java from cli

```bash
$ java -jar target/session_13_java-1.0.0.jar
```

### Before going to the next phase try IntelliJ 

Before going further, first `mvn clean` the project and then open the directory by IntelliJ IDE to see what's the difference in these two approach; **Maven (CLI) and IntelliJ (GUI)**.

### Declare dependencies

🛑 **Note-1**: We can comment java version in `pom.xml` file.

🛑 **Note-2**: If we comment the `build` section of `pom.xml` file everything works except we do not have a jar file. 

**Shoot for adding dependency:** 

Suppose that in addition to saying "Hello World!", you want the application to print the current date and time. While you could use the date and time facilities in the native Java libraries, you can make things more interesting by using the `Joda Time libraries`.

So, change the content of `HelloWorld.java` by this block of code:

```
package hello;

import org.joda.time.LocalTime;

public class HelloWorld {
  public static void main(String[] args) {
    LocalTime currentTime = new LocalTime();
    System.out.println("The current local time is: " + currentTime);
    Greeter greeter = new Greeter();
    System.out.println(greeter.sayHello());
  }
}
```

Add this dependency in the `pom.xml` file (See [here](https://mvnrepository.com/artifact/joda-time/joda-time))

```
<dependencies>
		<dependency>
			<groupId>joda-time</groupId>
			<artifactId>joda-time</artifactId>
			<version>2.12.17</version>
		</dependency>
</dependencies>
```

At this time your `pom.xml` file should look like this:

```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>ir.m-fozouni</groupId>
    <artifactId>session_13_java</artifactId>
    <packaging>jar</packaging>
    <version>0.1.0</version>


    <dependencies>
        <dependency>
            <groupId>joda-time</groupId>
            <artifactId>joda-time</artifactId>
            <version>2.9.2</version>
        </dependency>
    </dependencies>
<!-- joda-time -->  
    <dependencies>
		<dependency>
			<groupId>joda-time</groupId>
			<artifactId>joda-time</artifactId>
			<version>2.12.17</version>
		</dependency>
	</dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-shade-plugin</artifactId>
                <version>3.2.4</version>
                <executions>
                    <execution>
                        <phase>package</phase>
                        <goals>
                            <goal>shade</goal>
                        </goals>
                        <configuration>
                            <transformers>
                                <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                                    <mainClass>hello.HelloWorld</mainClass>
                                </transformer>
                            </transformers>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>

</project>
```

### Install again to see the result

```bash
$ mvn clean install 

$ java -jar target/session_13_java-0.1.0.jar
```

### Reference

1.  https://www.w3schools.com/java/java_intro.asp
2.  https://spring.io/guides/gs/maven#scratch 
3. https://codewithmosh.com/p/the-ultimate-java-mastery-series (I learned Java from this course)
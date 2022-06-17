import org.jetbrains.kotlin.gradle.tasks.KotlinCompile

plugins {
    id("com.digithurst.gradle.truststore") version "1.1.0"
    id("org.sonarqube") version "3.3"
    id("jacoco")
    id("org.jetbrains.kotlin.plugin.serialization") version "1.5.31"
    kotlin("jvm") version "1.5.31"
    application
}

group = "com.santander"
version = "0.0.1-SNAPSHOT"
java.sourceCompatibility = JavaVersion.VERSION_17

application {
    mainClass.set("ar.com.santander.docker.ApplicationKt")
}

repositories {
    maven {
        url = uri("http://nexus.iaas.ar.bsch/repository/maven-public/")
        isAllowInsecureProtocol = true
    }
}

dependencies {
    val ktorVersion = "1.6.4"
    val oracleVersion = "21.3.0.0"
    val exposedVersion = "0.35.1"
    val hikariVersion = "5.0.0"
    val brkrLibCoreKotlin = "1.1.15"
    val mockitoVersion = "3.12.4"

    implementation("io.ktor:ktor-server-core:$ktorVersion")
    implementation("io.ktor:ktor-server-netty:$ktorVersion")
    implementation("io.ktor:ktor-gson:$ktorVersion")
    implementation("io.ktor:ktor-server-tomcat:$ktorVersion")
    implementation("io.ktor:ktor-auth-jwt:$ktorVersion")
    implementation("io.ktor:ktor-auth:$ktorVersion")
    implementation("io.ktor:ktor-client-mock:$ktorVersion")

    implementation("io.ktor:ktor-client-logging-jvm:$ktorVersion")
    implementation("io.ktor:ktor-serialization:$ktorVersion")
    implementation("io.ktor:ktor-client-core:$ktorVersion")
    implementation("io.ktor:ktor-client-gson:$ktorVersion")

    implementation("org.jetbrains.kotlin:kotlin-reflect")
    implementation("org.jetbrains.kotlin:kotlin-stdlib-jdk8")

    implementation("co.elastic.apm:apm-agent-api:1.26.0")
    implementation("org.postgresql:postgresql:42.2.23")
    implementation("com.zaxxer:HikariCP:$hikariVersion")

    implementation("org.jetbrains.exposed:exposed-core:$exposedVersion")
    implementation("org.jetbrains.exposed:exposed-dao:$exposedVersion")
    implementation("org.jetbrains.exposed:exposed-jdbc:$exposedVersion")
    implementation("org.jetbrains.exposed:exposed-java-time:$exposedVersion")

    implementation("com.oracle.database.jdbc:ojdbc8:$oracleVersion")

    implementation("ch.qos.logback:logback-classic:1.2.6")

    implementation("com.auth0:auth0:1.34.1")
    implementation("com.auth0:java-jwt:3.18.2")

    implementation("org.kodein.di:kodein-di-jvm:7.8.0")

    testImplementation("org.mockito.kotlin:mockito-kotlin:3.2.0")
    testImplementation("org.mockito:mockito-inline:$mockitoVersion")
    testImplementation("org.mockito:mockito-core:$mockitoVersion")

    implementation("ar.com.santander:brkr-lib-core-kotlin:$brkrLibCoreKotlin")

    testImplementation("io.ktor:ktor-server-test-host:$ktorVersion")
    testImplementation("org.junit.jupiter:junit-jupiter:5.8.1")
    testImplementation("com.h2database:h2:1.4.200")
}

tasks.withType<Test> {
    useJUnitPlatform()
}

tasks.withType<KotlinCompile> {
    kotlinOptions {
        freeCompilerArgs = listOf("-Xjsr305=strict")
        jvmTarget = "16"
    }
}

jacoco {
    toolVersion = "0.8.7"
}

tasks.jacocoTestReport {
    reports {
        xml.isEnabled = true
        csv.isEnabled = false
        html.isEnabled = true
        html.destination = file("$buildDir/reports/coverage")
    }

    classDirectories.setFrom(
        sourceSets.main.get().output.asFileTree.matching {
            //exclude("**/dto/**")
        }
    )
}

sonarqube {
    properties {
        property("sonar.coverage.jacoco.xmlReportPaths", "$buildDir/reports/jacoco/test/jacocoTestReport.xml")
    }
}

tasks.withType<Jar> {
    manifest {
        attributes["Main-Class"] = application.mainClass
    }
    from({
        configurations.runtimeClasspath.get().filter { it.name.endsWith("jar") }.map { zipTree(it) }
    })
    duplicatesStrategy = DuplicatesStrategy.EXCLUDE
}

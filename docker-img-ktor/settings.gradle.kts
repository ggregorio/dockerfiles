rootProject.name = "docker-image"
pluginManagement {
    repositories {
        /*
        maven(
            "http://nexus.iaas.ar.bsch/repository/maven-public/",
            "true"
        )
        */
        maven {
            url = uri("http://10.70.1.10/repository/maven-public/")
            isAllowInsecureProtocol = true
        }
    }
}
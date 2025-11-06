package com.ex.bg

interface Platform {
    val name: String
}

expect fun getPlatform(): Platform
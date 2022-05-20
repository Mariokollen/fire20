function Gjennomsnitt (tall: number, tall2: number, tall3: number) {
    rødt = Math.round((tall + tall2 + tall3) / 3)
}
let blå = 0
let grønt = 0
let rødt = 0
let tabell = [0, 1]
let strip = neopixel.create(DigitalPin.P0, 30, NeoPixelMode.RGB)
strip.showColor(neopixel.colors(NeoPixelColors.Black))
strip.setBrightness(200)
for (let indeks = 0; indeks <= strip.length(); indeks++) {
    tabell.push(0 + 100)
}
basic.forever(function () {
    for (let indeks = 0; indeks <= strip.length(); indeks++) {
        if (Math.randomBoolean()) {
            Gjennomsnitt(randint(0, 100), rødt, tabell[indeks])
        } else {
            Gjennomsnitt(0, rødt, tabell[indeks])
        }
        grønt = randint(0, rødt * 0.25)
        blå = randint(0, rødt * 0.1)
        tabell[indeks] = rødt
        strip.setPixelColor(indeks, neopixel.rgb(rødt, grønt, blå))
    }
    strip.show()
    basic.pause(randint(700, 1200))
})

func countStudents(students []int, sandwiches []int) int {
    attempts_per_sandwich := 0
    for len(students)>0 && attempts_per_sandwich < len(students){
        first_student := students[0]
        first_sandwich := sandwiches[0]

        if first_student == first_sandwich{
            attempts_per_sandwich = 0
            students = students[1:]
            sandwiches = sandwiches[1:]
        } else {
            attempts_per_sandwich = attempts_per_sandwich + 1
            students = students[1:]
            students = append(students, first_student)
        }
        fmt.Println(students)
    }
    return len(students)
}

Exercício de fila. Precisava praticar, bem simplesinho. Vamos lá, a primeira coisa que eu faço é fazer um while (sim, eu tambem estranhei a forma que o for é feito em go), esse while ocorre enquanto o array tiver mais que um item e a variavel attempts_per_sandwich for menor que o numero de pessoas da que estao na fila de estudantes. Essa variável é importante pois, ela conta cada tentativa (pessoa) para cada um dos sanduiches, se nenhum comer o sanduiche acabou e deve retornar o tamanho do array restante. Se o camarada comer o sanduiche, ele sai das filas principais, assim como o sanduiche (obviamente pois ele foi comido), se não o usuario vai pro final da fila e sanduiche continua na posicao.
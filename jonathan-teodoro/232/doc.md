type MyQueue struct {
    stack []int

}


func Constructor() MyQueue {
    return MyQueue{
        stack: []int{},
    }
}


func (this *MyQueue) Push(x int)  {
    this.stack = append(this.stack, x)
}


func (this *MyQueue) Pop() int {
    last := this.stack[0]
    this.stack = this.stack[1:]
    return last
}   


func (this *MyQueue) Peek() int {
    return this.stack[0]
}


func (this *MyQueue) Empty() bool {
    if len(this.stack) < 1{
        return true
    }
    return false
}


Exercicio simples de TAD de fila. Nada de muito complexo. Um push para o enqueue, um pop para o dequeue. Uma função que retorna o exercício da frente da fila e uma que retorna se ta vazia ou não. Treinei manipulação de slices, nunca fui muito bom fazendo essa manipulação, em nenhuma linguagem. Acho que to pegando a manhã. 

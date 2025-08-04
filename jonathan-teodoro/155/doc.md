type MinStack struct {
    stack []int
}

func Constructor() MinStack {
    return MinStack{
        stack: []int{},
    }
}

func (this *MinStack) Push(val int)  {
    this.stack = append(this.stack, val)
}

func (this *MinStack) Pop()  {
   this.stack = this.stack[:len(this.stack)-1]
}

func (this *MinStack) Top() int {
    return this.stack[len(this.stack)-1]
}

func (this *MinStack) GetMin() int {
    min_value := this.stack[0]
    for _,value := range this.stack{
        if value < min_value{
            min_value = value
        }    
    }
    return min_value
}


/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */

Tadzinho simples de fila, bem tranquilinho, aproveitei para treinar fundamentos de go, como o slice do ultimo item com [:len(s)-1]. Fiz um loopzinho for na funcao de retornar o menor valor. De resto, tudo bem simples.
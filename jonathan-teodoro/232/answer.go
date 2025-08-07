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


/**
 * Your MyQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Peek();
 * param_4 := obj.Empty();
 */

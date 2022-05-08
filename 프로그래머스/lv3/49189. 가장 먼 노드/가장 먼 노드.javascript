function solution(n, edge) {
    var answer = 0;
    var visited = Array(n+1).fill(0);
    var lev = Array(n+1).fill(0);
    const queue = [1];
    visited[1] = 1
    while(queue.length){
        const cur = queue.shift();
        const cur_lev = lev[cur]+1
        for (let node of edge){
            if (cur==4){
            }
            if(node[0] === cur && !visited[node[1]]){
                queue.push(node[1])
                visited[node[1]] = 1
                lev[node[1]] = cur_lev;
            }
            else if(node[1] === cur && !visited[node[0]]){
                queue.push(node[0])
                visited[node[0]]=1
                lev[node[0]] = cur_lev;
            }
        }
    }
    const max_cost = Math.max.apply(null,lev)
    const res = lev.filter((prev)=>prev===max_cost).length
    
    return res;
}
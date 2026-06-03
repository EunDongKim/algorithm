def solution(video_len, pos, op_start, op_end, commands):
    pos = int(pos[0:2])*60 + int(pos[3:])
    video_len = int(video_len[0:2])*60 + int(video_len[3:])
    op_start = int(op_start[0:2])*60 + int(op_start[3:])
    op_end = int(op_end[0:2])*60 + int(op_end[3:])
    commands.append("end")
    for command in commands:
        if 0 > pos : pos = 0
        if video_len < pos : pos = video_len
        if pos >= op_start and pos < op_end: pos = op_end
        if command == "next": pos += 10
        elif command == "prev": pos -= 10
    
    return f"{pos//60:02}:{pos%60:02}"

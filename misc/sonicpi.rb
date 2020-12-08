loop do
  with_synth :dsaw do
    with_fx(:slicer, phase: [0.25,0.125].choose) do
      with_fx(:reverb, room: 0.5, mix: 0.3) do
        start_note = chord([:b1, :b2, :e1, :e2, :b3, :e3].choose, :minor).choose
        final_note = chord([:b1, :b2, :e1, :e2, :b3, :e3].choose, :minor).choose
        
        p = play start_note, release: 8, note_slide: 4, cutoff: 30, cutoff_slide: 4, detune: rrand(0, 0.2), pan: rrand(-1, 0), pan_slide: rrand(4, 8)
        control p, note: final_note, cutoff: rrand(80, 120), pan: rrand(0, 1)
      end
    end
  end
  sleep 8
end

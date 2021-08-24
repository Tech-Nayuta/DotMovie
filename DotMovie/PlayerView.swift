//
//  PlayerView.swift
//  DotMovie
//
//  Created by 化田晃平 on R 3/08/24.
//

import SwiftUI
import AVKit

struct PlayerView: UIViewRepresentable {
    let player: AVPlayer

    func updateUIView(_ uiView: UIView, context: UIViewRepresentableContext<PlayerView>) {
    }

    func makeUIView(context: Context) -> UIView {
        player.play()
        return PlayerUIView(player: player)
    }
}

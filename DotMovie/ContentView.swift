//
//  ContentView.swift
//  DotMovie
//
//  Created by 化田晃平 on R 3/08/24.
//

import SwiftUI
import AVKit

struct ContentView: View {
    private let player: AVPlayer = AVPlayer(url: URL(fileURLWithPath: Bundle.main.path(forResource: "pict", ofType: "mp4")!))
    var body: some View {
        GeometryReader { bodyView in
            VStack {
                PlayerView(player: self.player)
            }.frame(width:bodyView.size.width, height:bodyView.size.width)
        }
    }

    private func movieStart() {
        self.player.seek(to: CMTime(seconds: 0, preferredTimescale: 600))
        self.player.play()
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

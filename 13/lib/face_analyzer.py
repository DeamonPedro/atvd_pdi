
from collections import deque
from typing import Deque, Tuple

from cv2 import Mat
import lib.face_utils as face_utils


class FaceAnalyzer():
    identified_faces = []
    last_face_identified_id = None

    def __init__(self, min_similarity=0.8, face_bank_len=30) -> None:
        self.min_similarity = min_similarity
        self.face_bank_len = face_bank_len

    def identify_face(self, face: Mat) -> Tuple[int, float]:
        if self.last_face_identified_id != None:
            similarity_last = self.calc_similarity(
                face, self.identified_faces[self.last_face_identified_id])
            if similarity_last >= self.min_similarity:
                self.save_face_frame(face, self.last_face_identified_id)
                return self.last_face_identified_id, similarity_last
        face_id, similarity = self.search_face(face)
        if face_id == None:
            face_id, similarity = (len(self.identified_faces), 1)
            print(f'new face found - id: {face_id}')
        self.save_face_frame(face, face_id)
        self.last_face_identified_id = face_id
        return face_id, similarity

    def search_face(self, face: Mat) -> Tuple[int or None, float or None]:
        for face_id, faces in enumerate(self.identified_faces):
            similarity = self.calc_similarity(face, faces)
            if similarity >= self.min_similarity:
                return face_id, similarity
        return None, None

    def calc_similarity(self, face1: Mat, faces: Deque) -> float:
        similarity_list = []
        for face2 in faces:
            similarity = face_utils.calc_similarity_between_faces(face1, face2)
            similarity_list.append(similarity)
            if similarity >= self.min_similarity or similarity <= 0.65:
                break
        return max(similarity_list)

    def save_face_frame(self, face: Mat, face_id: int) -> None:
        if face_id >= len(self.identified_faces):
            self.identified_faces.append(deque([face], self.face_bank_len))
        else:
            self.identified_faces[face_id].appendleft(face)
